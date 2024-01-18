import json
from typing import Iterable

import scrapy
from scrapy import Request

from maotuying.items import MaotuyingItem


class ChinaToursSpider(scrapy.Spider):
    name = "china_tours"
    allowed_domains = ["www.tripadvisor.cn", "api.tripadvisor.cn"]

    def start_requests(self) -> Iterable[Request]:
        base_url = "https://api.tripadvisor.cn/restapi/soa2/20405/getPCSightList"
        headers = {
            "Host": " api.tripadvisor.cn",
            "User-Agent": " Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:120.0) Gecko/20100101 Firefox/120.0",
            "Accept": " */*",
            "Accept-Language": " en-US,en;q=0.5",
            "Accept-Encoding": " gzip, deflate, br",
            "Referer": " https://www.tripadvisor.cn/",
            "content-type": " application/json;charset:utf-8;",
            "Origin": " https://www.tripadvisor.cn",
            "Connection": " keep-alive",
            "Sec-Fetch-Dest": " empty",
            "Sec-Fetch-Mode": " cors",
            "Sec-Fetch-Site": " same-site",
        }
        for page in range(1, 334):
            post_data = {
                "geoId": 294211,
                "pageIndex": page,
                "pageSize": 30,
                "travelRanking": False,
                "needSelectedFilters": True,
                "filters": [
                    {"type": "subcategory", "param": ""},
                    {"type": "subtype", "param": ""},
                    {"type": "neighborhood", "param": ""},
                    {"type": "travelerRating", "param": ""},
                    {"type": "awards", "param": ""},
                    {"type": "waypointairport", "param": ""},
                    {"type": "waypointstation", "param": ""},
                    {"type": "other", "param": ""},
                ],
            }
            post_data = json.dumps(post_data)
            yield scrapy.Request(
                url=base_url,
                method="POST",
                headers=headers,
                body=post_data,
                callback=self.parse,
            )

    def parse(self, response):
        data = json.loads(response.text)
        tours = data["verticalData"]
        for tour in tours:
            # 景点ID
            location_id = tour["taSightId"]
            # 景点名
            display_name = tour["displayName"]
            # 景点详细页URL
            url = tour["url"]
            # 景点封面图
            image = tour["coverImage"]["url"]
            # 评价人数
            reviews_count = tour["reviewsCount"]
            # tag 描述
            tags_desc = tour["tagsDesc"]
            item = MaotuyingItem(
                location_id=location_id,
                display_name=display_name,
                url="https://www.tripadvisor.cn/" + url,
                cover_image=str(image),
                reviews_count=reviews_count,
                tags_desc=tags_desc,
            )

            base_next_url = (
                "https://api.tripadvisor.cn/restapi/soa2/20405/getPCSightDetailInfo"
            )
            post_data = {"locationId": location_id}
            post_data = json.dumps(post_data)
            yield scrapy.Request(
                url=base_next_url,
                method="POST",
                body=post_data,
                callback=self.parse_detail,
                meta={"item": item},
            )

    def parse_detail(self, response):
        item = response.meta["item"]
        data = json.loads(response.text)
        sightBasicInfo = data["sightBasicInfo"]
        # 所在地址
        address = sightBasicInfo["address"]
        # 评分
        review_rating = sightBasicInfo["reviewRating"]
        # 特色评论
        feature_reviews = data["featureReviews"]
        feature_reviews = [review["content"] for review in feature_reviews]
        yield MaotuyingItem(
            location_id=item["location_id"],
            display_name=item["display_name"],
            url=item["url"],
            cover_image=item["cover_image"],
            reviews_count=item["reviews_count"],
            tags_desc=item["tags_desc"],
            address=address,
            review_rating=review_rating,
            feature_reviews=feature_reviews,
        )
