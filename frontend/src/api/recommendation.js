import request from '@/utils/request'

const recommendationRequest = {
    getRecommendedLandscapesByUserId: (pid) => {
        return request({
            url: `/api/recommendation${pid}`,
            method: 'get',
        })
    },
}