import VueRouter from "vue-router";
import AboutLife from '../pages/AboutLife.vue'


export default new VueRouter({
    routes:[
        {
            path:'/aboutlearn',
            component:AboutLife,
        },
        {
            path:'/aboutwork',
            component:AboutLife,
            
        },
        {
            path:'/aboutlife',
            component:AboutLife
        }
    ]
})