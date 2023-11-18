import VueRouter from "vue-router";

// import AboutLearn from '../pages/AboutLearn.vue'
// import AboutWork from '../pages/AboutWork.vue'
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