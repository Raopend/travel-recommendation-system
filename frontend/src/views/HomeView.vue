<script setup>
import ToursCarousel from "@/components/home/ToursCarousel.vue";
import ToursList from "@/components/home/ToursList.vue";
import {ref} from "vue";

const tags = ref(['猜你喜欢', '最多人去', '评分最高', '今日热门', '旅行地Top100',])
</script>

<template>
    <div class="flex-container">
        <ToursCarousel/>
    </div>
    <ToursList
        :opt="2"
        :tag="tags[1]"
        class="LandscapeList my-border"
    />
</template>

<style scoped>
.flex-container {
    display: flex;
    flex-wrap: wrap;

    margin-top: 0.5rem;
    margin-left: 25%;
    margin-right: 25%;
}

.LandscapeList {
    padding: 1rem;
    margin: 1rem 20% 1rem 20%;
}

@media screen and (max-width: 1200px) {
    .flex-container {
        margin-left: 5%;
        margin-right: 5%;
    }

    .LandscapeList {
        margin-left: 0;
        margin-right: 0;
    }
}

.top-left-image {
    position: relative;
    top: 50px;
    left: -100px;
    width: 100px; /* 根据需要调整图片的宽度 */
    height: 100px; /* 根据需要调整图片的高度 */
    //z-index: 1000;
}
</style>