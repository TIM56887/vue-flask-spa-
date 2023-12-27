import HousePricePredict from "../pages/HousePricePredict.vue";
import HomeMain from "../pages/HomeMain.vue"
import VueRouter from "vue-router";


export default new VueRouter({
    mode:'history',
    routes:[
        {
            path:'/housepricepredict',
            component:HousePricePredict,
        },
        {
            path:'/',
            component:HomeMain,
            
        },
        // {
        //     path:'/aboutlife',
        //     component:AboutLife
        // }
    ]
})