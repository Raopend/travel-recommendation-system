<script setup>
import {Lock as IconLock, User as IconUser} from '@element-plus/icons-vue'
import {reactive, ref, unref} from "vue";
import {useRouter} from "vue-router";
import {ElMessage} from "element-plus";
import userRequest from "@/api/user.js";

const router = useRouter();
// 是否记住密码
let remember = ref(false);
// 登录表单
const loginFormRef = ref('');
const loginForm = reactive({
    login: '',
    password: '',
})
// 定义表单验证规则
const rules = reactive({
    login: [
        {required: true, message: '请输入账号', trigger: 'blur'},
        {min: 4, max: 20, message: '长度在4到20个字符', trigger: 'blur'}
    ],
    password: [
        {required: true, message: '请输入密码', trigger: 'blur'},
        {min: 4, max: 20, message: '长度在4到20个字符', trigger: 'blur'}
    ],
})

const postLogin = (async () => {
    const form = unref(loginFormRef);
    if (!form) {
        return;
    }
    try {
        await form.validate();
        userRequest.login(loginForm).then(res => {
            if (res.code === 200) {
                // 登录成功之后，将 token 保存到 localStorage 中
                localStorage.setItem("token", res.data.token);
                ElMessage.success("登录成功")
                // 登录成功之后，进行页面跳转
                router.replace("/");
            } else {
                ElMessage.error("登录失败");
            }
        }).catch(err => {
            console.log(err);
        })
    } catch (err) {
        console.log(err);
    }

    // 继续请求 profile 接口，获取用户信息
    userRequest.getUserInfo(loginForm.login).then(res => {
        if (res.code === 200) {
            localStorage.setItem("userInfo", JSON.stringify(res.data));
        }
    }).catch(err => {
        console.log(err);
    })
})
</script>

<template>
    <div class="flex min-h-full flex-col justify-center px-6 py-12 lg:px-8">
        <div class="sm:mx-auto sm:w-full sm:max-w-sm" @keyup.enter="postLogin">
            <img class="mx-auto h-10 w-auto" src="@/assets/travel-book.png" alt="logo"/>
            <h2 class="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">
                旅行推荐系统-登陆</h2>
            <div class="mt-10 text-center text-sm text-gray-500">
                <el-link href="/register" :underline="false"
                         class="font-semibold leading-6 text-indigo-600 hover:text-indigo-500">
                    还没有账号？去注册
                </el-link>
            </div>
        </div>

        <el-form ref="loginFormRef" :model="loginForm" :rules="rules" class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
            <el-form-item label="账 号" prop="login">
                <el-input class="login-form-input" placeholder="账 号" v-model="loginForm.login" autofocus
                          autocomplete="off">
                    <template #prefix>
                        <el-icon class="el-input__icon">
                            <icon-user/>
                        </el-icon>
                    </template>
                </el-input>
            </el-form-item>

            <el-form-item label="密 码" prop="password">
                <el-input class="login-form-input" placeholder="密 码" v-model="loginForm.password" show-password>
                    <template #prefix>
                        <el-icon class="el-input__icon">
                            <icon-lock/>
                        </el-icon>
                    </template>
                </el-input>
            </el-form-item>

            <div class="scan-and-forget-div">
                <el-link href="/forget" class="my-font" :underline="false">忘记密码?</el-link>
            </div>

            <el-form-item>
                <el-button @click="postLogin" class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600" type="primary">登 录</el-button>
            </el-form-item>
        </el-form>
    </div>
</template>
