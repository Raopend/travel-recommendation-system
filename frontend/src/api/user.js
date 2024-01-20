import request from '@/utils/request'

const userRequest = {
    /**
     * 用户登录
     * @param loginForm
     * @returns {*}
     */
    login: (loginForm) => {
        return request({
            url: '/api/user/login/',
            method: 'post',
            headers: {
                isNeedToken: false
            },
            data: loginForm
        })
    },
    /**
     * 用户注册
     * @param registerForm
     * @returns {*}
     */
    register: (registerForm) => {
        return request({
            url: '/api/user/register/',
            method: 'post',
            headers: {
                isNeedToken: false
            },
            data: registerForm
        })
    },
    /**
     * 用户注销登录
     * @returns {*}
     */
    logout: () => {
        return request({
            url: '/api/user/logout/',
            method: 'post',
            headers: {
                isNeedToken: true
            },
        })
    },
    /**
     * 修改密码
     * @param updatePasswordForm
     */
    updatePassword: (updatePasswordForm) => {
        return request({
            url: '/api/user/reset-password/',
            method: 'post',
            headers: {
                isNeedToken: true,
            },
            data: updatePasswordForm
        })
    },
    /**
     * 判断token是否过期
     * @returns {*}
     */
    judge: () => {
        return request({
            url: '/user/judge',
            method: 'post',
            headers: {
                isNeedToken: true
            },
        })
    },
    /**
     * 获取当前登录用户的基本信息
     * @returns {*}
     */
    getUserInfo: (username) => {
        return request({
            url: `/api/user/userinfo/${username}/`,
            method: 'get',
        })
    },
}

export default userRequest
