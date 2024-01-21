import request from '@/utils/request'

const recommendationRequest = {
    getRecommendedLandscapesByUserId: (id) => {
        return request({
            url: `/api/recommendation/${id}/`,
            method: 'get',
        })
    },
}
export default recommendationRequest