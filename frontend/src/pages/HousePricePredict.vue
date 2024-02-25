<template>
    <div>
        <HousePricePreview />
        <HousePrice class="p-5"/>
    </div>
</template>
<script>
import HousePrice from '@/components/HousePrice/HousePrice.vue';
import HousePricePreview from '@/components/HousePrice/HousePricePreview.vue';

export default{
    components:{
        HousePrice,
        HousePricePreview
    }
}

</script>

<style scoped>

</style>