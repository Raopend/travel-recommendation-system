<script setup>

import LandscapeFooter from "@/components/layout/Footer.vue";
import LandscapeHeader from "@/components/layout/Header.vue";
</script>

<template>
    <el-container>
        <LandscapeHeader class="header"/>

        <el-main class="content" style="padding: 0">
            <router-view/>
        </el-main>

        <el-footer class="footer" style="padding: 0">
            <LandscapeFooter/>
        </el-footer>

    </el-container>
</template>

<style scoped>

</style>