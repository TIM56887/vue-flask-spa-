<template>
    <div class="mytodo">
        <div class="mytodotitle">
            <i class="bi bi-list-task"></i>
            <div class="titletext">TO-DO List</div>
        </div>
        <ul class="mytodoul">
            <TodoItem v-for="todo,index in mytodo" :key="index" :todo="todo"/>
        </ul>
    </div>

</template>
s
<script>
import { mapState } from 'vuex'
import TodoItem from './TodoItem.vue'
export default {
    name:'MyTodo',
    components:{
        TodoItem
    },
    data(){
        return{
            mytodo:[{content:'學React',date:'7/10'},{content:'學Tailwind',date:'7/13'}]
            
        }
    },
    methods:{
        changemode(){
            this.$store.commit('CHANGEMODE')
        }
    },
    computed:{
        ...mapState(['theme'])
    }
}
</script>

<style scoped>

@media (min-width: 768px) {

        i {
            width:15%;
        }
        .mytodotitle{
            margin:2rem 0 0 0;
            font-weight: 500;   
            font-size: 1.8rem;
            display: flex;
        }
        .mytodo {
            display: flex;
            flex-direction: column;
            width:30vw;
            height: 70%;
            /* text-align: center; */
            background-color:#fff;
            border-radius: 2rem;
            padding: 0 0 0 50px;
            border: 2px solid #ccc;
            box-shadow: 0 0 10px rgba(0,0,0,.1);
        }

        ul {
            padding: 0 0 0 20px;
        }
    }

    

    @media (max-width:768px) {
        .mytodo {
            display: flex;
            flex-direction: column;
            width:70vw;
            height: 30%;
            /* height: 1000px; */
            background-color:#fff;
            border-radius: 2rem;
            padding: 0 0 0 50px;
            border: 2px solid #ccc;
            box-shadow: 0 0 10px rgba(0,0,0,.1);
            margin-bottom: 20px;
        }

        ul {
            padding: 0 0 0 0;
            margin:0;
        }
        .mytodotitle{
            margin:2rem 0 0 0;
            font-weight: 500;   
            font-size: 1.8rem;
            display: flex;
        }
        i {
            width:40px;
        }


    }
</style>