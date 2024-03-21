<script setup>
import {Menu} from "@element-plus/icons-vue";
import {onBeforeMount, onBeforeUnmount, reactive, ref, watch} from "vue";
import {useRouter} from 'vue-router';
import userRequest from "@/api/user.js";
import {ElMessage} from "element-plus";
import emitter from "@/utils/event-bus";

const router = useRouter();
let isLogin = ref(false);
let isShowMenu = ref(false);
let mainMenuRef = ref(null);
let moreRef = ref(null);
let moreFilledRef = ref(null);
let iconColor = ref('white')
let user = reactive({
    id: 0,
    nickname: '',
    avatar: '',
    sex: '',
});

// 展示名为 name 的页面
let show = (name) => {
    router.push({
        name: name
    })
    isShowMenu.value = false;
}

// 控制主菜单显示
let handleMainMenu = () => {
    isShowMenu.value = !isShowMenu.value;
}
// 监测主菜单显示变量，根据展示与否改变图标颜色
watch(isShowMenu, (newValue, oldValue) => {
    if (newValue === true) {
        iconColor.value = '#a99f9f';
    } else {
        iconColor.value = 'white'
    }
})

// 跳转到登录界面
let handleLogin = () => {
    router.push('/login');
}

// 登出
let handleLogout = () => {
    userRequest.logout().then(res => {
        if (res.code === 200) {
            ElMessage.success("注销成功");
            // 用户注销时将缓存中的token和userInfo删除
            localStorage.removeItem('token');
            localStorage.removeItem('userInfo');
            isLogin.value = false;
            router.replace({
                name: 'home'
            });
        } else {
            ElMessage.error("注销失败");
        }
    }).catch(err => {
        ElMessage.error(err);
    })
}
const userInfoJSON = localStorage.getItem('userInfo');

// 将 JSON 字符串解析为 JavaScript 对象
const userInfo = JSON.parse(userInfoJSON);
console.log(userInfo);
/**
 * 每次初始化界面是判断token是否过期，如果没有过期，则显示登录基本信息
 */
userRequest.getUserInfo(userInfo.username).then(res => {
    if (res.code === 200) {
        isLogin.value = true
        let userInfo = res.data
        user.nickname = userInfo.username
        user.id = userInfo.id
        user.avatar = userInfo.avatar
    } else {
        isLogin.value = false
    }
}).catch(err => {
    console.log(err)
    console.error(err)
});

const errorHandler = () => true;

/**
 * 监听nickname和avatar的改变
 */
emitter.on('handleHeaderNicknameChange', data => {
  user.nickname = data.nickname
})
emitter.on('handleHeaderAvatarChange', data => {
  user.avatar = data.avatar
})
</script>

<template>
    <div class="navbar">
        <div class="logo">
            <img src="@/assets/travel-book.png" style="width: 75px; height: 75px; float: left; padding-right: 40px;"
                 alt="logo"/>
            <span class="title">旅行推荐系统</span>
        </div>

        <div @click="handleMainMenu" class="menu-icon">
            <div ref="moreRef">
                <Menu :color="`${iconColor}`"/>
            </div>
        </div>

        <div class="big-menu">
            <el-link @click="show('home')" :underline="false">首页</el-link>
<!--            <el-link @click="show('dashboard')" :underline="false">大数据统计</el-link>-->
            <el-link @click="show('recommend')" :underline="false">猜你喜欢</el-link>
        </div>

        <el-link
            class="login-link"
            v-if="!isLogin"
            @click="handleLogin"
            :underline="false"
        >
            登录
        </el-link>
        <el-dropdown class="login-dropdown" v-if="isLogin">
            <el-button type="text">
                <div class="login-name">
                    {{ user.nickname }}
                </div>
                <el-avatar :src="user.avatar" @error="errorHandler">
                    <!-- 当图片加载错误时，将加载这里面的图片 -->
                    <img src="@/assets/default_avatar.png" alt="default avatar"/>
                </el-avatar>
            </el-button>

            <template #dropdown>
                <el-dropdown-menu>
                    <el-dropdown-item>
                        <el-link :underline="false" @click="show('personal')" style="padding-right: 7px">
                            <i style="padding-right: 3px"></i>我的主页
                        </el-link>
                    </el-dropdown-item>
                    <el-dropdown-item>
                        <el-link :underline="false" @click="show('personalPlanet')" style="padding-right: 7px">
                            <i style="padding-right: 3px"></i>电影星球
                        </el-link>
                    </el-dropdown-item>
                    <el-dropdown-item>
                        <el-link :underline="false" @click="show('setting')" style="padding-right: 7px">
                            <i style="padding-right: 3px"></i>个人设置
                        </el-link>
                    </el-dropdown-item>
                    <el-dropdown-item divided>
                        <el-button type="text" @click="handleLogout" :underline="false">
                            <i style="padding-right: 3px"></i>退出登录
                        </el-button>
                    </el-dropdown-item>
                </el-dropdown-menu>
            </template>
        </el-dropdown>
    </div>
</template>

<style scoped>
/* 设置顶部导航栏样式 */
.navbar {
    z-index: 500;
    height: 50px;
    padding-left: 10%;
    padding-right: 10%;
    display: flex;
    background-color: rgb(84, 92, 100);
}

/*系统logo图片和字体样式*/
.logo {
    display: flex;
    align-items: center;
    height: 50px;

    img {
        padding-top: 5px;
        width: 40px;
        height: 40px;
    }

    .title {
        color: #dddddd;
        font-size: 30px;
    }
}

.menu-icon {
    display: none;
}

.big-menu {
    display: flex;
}

.menu {
    display: none;
}

/* 设置导航条链接演示 */
.navbar a {
    font-size: 20px;
    color: white;

    padding: 12px 20px;
    text-decoration: none;
    text-align: center;
}

/* 更改鼠标悬停时的颜色 */
.navbar a:hover {
    color: white;
    animation: heartBeat;
    animation-duration: 0.7s;
}

/*搜索框样式*/
.search-div {
    width: 600px;
    padding-top: 10px;
    text-align: center;
}

/*登录样式*/
.login-link {
    margin-left: auto; /*右对齐*/
}

/*登录成功抽屉样式*/
.login-dropdown {
    margin-top: auto;
    margin-bottom: auto;
    margin-left: auto;

    /*登录用户名样式*/

    .login-name {
        font-weight: bolder;
        font-size: 15px;
        letter-spacing: 2px;
    }
}

/* 响应式布局 - 当屏幕小于 740 像素宽 */
@media screen and (max-width: 740px) {
    .navbar {
        z-index: 999;
        padding: 0 1rem;
    }

    .menu-icon {
        order: 1;
        display: block;
        width: 2rem;
        height: 2rem;
        position: relative;
        margin: auto 0;
    }

    .big-menu {
        display: none;
    }

    .menu {
        order: 5;
        position: absolute;
        left: 0;
        top: 50px;
        width: 100%;
        z-index: 500;
        background-color: #333;
        flex-direction: column;
        display: flex;

        .search-div {
            margin-left: auto;
            margin-right: auto;
            margin-bottom: 10px;
        }
    }

    .logo {
        position: absolute;
        left: 45%;

        .title {
            display: none;
        }
    }

    .login-link,
    .login-dropdown {
        order: 3;
    }

    .menu-enter-active {
        animation: show-menu 0.5s linear;
    }

    .menu-leave-active {
        animation: show-menu 0.5s reverse;
    }

    @keyframes show-menu {
        from {
            z-index: -100;
            transform: translateY(-100%);
        }

        to {
            z-index: 500;
            transform: translateY(0%);
        }
    }
}

/* 响应式布局 - 当屏幕为（740px < 屏幕像素 < 1200px)宽 时，系统名消失，并且左右内边距变为0 */
@media screen and (min-width: 740px) and (max-width: 1200px) {
    /* 左右内边距变为0 */
    .navbar {
        padding-left: 0;
        padding-right: 0;
    }

    /* logo名消失 */
    .logo .title {
        display: none;
    }

    .big-menu {
        display: flex;
    }

    .menu {
        display: none;
    }
}
</style>