<template>
    <div>
        <PortfolioResume />
        <PortfolioList />
        <LearningResource />
        <CommentSection />
        <AboutMe />
    </div>
</template>

<script>
import AboutMe from "../components/Home/AboutMe.vue"
import LearningResource from "../components/Home/LearningResource"
import PortfolioList from "../components/Home/PortfolioList.vue"
import PortfolioResume from "../components/Home/PortfolioResume.vue"
import CommentSection from "../components/Home/CommentSection.vue"

export default{
    components:{
        PortfolioResume,
        PortfolioList,
        LearningResource,
        AboutMe,
        CommentSection
    }
}

</script>

<style>

</style>