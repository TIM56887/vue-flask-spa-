<template>
    <div>
        <HousePricePreview v-if="showpreview" @changePage="changePage"/>
        <HousePrice v-else @changePage="changePage" class="p-5"/>
    </div>
</template>
<script>
import HousePrice from '@/components/HousePrice/HousePrice.vue';
import HousePricePreview from '@/components/HousePrice/HousePricePreview.vue';

export default{
    components:{
        HousePrice,
        HousePricePreview
    },
    data(){
        return{
            showpreview: true,
        }
    },
    methods:{
        changePage(){
            this.showpreview = !this.showpreview;
        }
    }
}

</script>

<style scoped>

</style>