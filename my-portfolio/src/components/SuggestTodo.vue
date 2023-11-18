<template>
    <section class="comment-area">
        <div class=" d-flex flex-column">
            <h1>
                <div class="text-center fs-3">
                    Comment . . .
                </div>
            </h1>
            <div class="suggestTodo h-100 d-flex flex-column  ">
                <div class="showlist mt-4 h-75">
                    <ul>
                        <SuggestTodoItem v-for="todo in todo" :key=todo.id :todo="todo"/>
                    </ul>
                </div>
                <div class="d-flex justify-content-center input-box">
                    
                    <div class="input-group input-group-lg shadow-sm mx-5 bg-body-tertiary rounded" >
                    <span class="input-group-text input-title" id="inputGroup-sizing-lg">留言．．．</span>
                    <input
                        type="text" 
                        class="form-control fs-5 " 
                        aria-label="Sizing example input" 
                        aria-describedby="inputGroup-sizing-lg"
                        placeholder="your input is always good . . ." 
                        maxlength="100"
                        @keydown.enter="addnewtodo" 
                        v-model="inputData"
                    >
                    
                    </div>
                </div>
                
            </div>
        </div>
    </section>
</template>

<script>
import { mapState } from 'vuex'
import SuggestTodoItem from './SuggestTodoItem.vue';
export default {
    name:'SuggestTodo',
    components:{
        SuggestTodoItem
    },
    data() {
        return {
            
            user:'',
            inputData:''
        };
    },
    methods:{
        toggleLike() {
            this.liked = !this.liked;
        },
        addnewtodo(e){ 
            e.preventDefault();
            
            if (this.inputData){
                const data = {
                    createtime:new Date(),
                    content:e.target.value,
                    userid:this.user
                }
                this.inputData = "" 
                this.$store.dispatch('SendTodo',data)
            }
            
        },
        deletetodo(id){
            console.log(id)
            this.$store.dispatch('deletetodo',id)
        }
    },
    computed:{
        ...mapState(['todo']),
    },
    mounted(){
        this.$store.dispatch('gettodo')
        if(localStorage.getItem('userId')) {
            this.$store.dispatch('getusertodo',localStorage.getItem('userId'))
            this.user = localStorage.getItem('userId')
        }
        console.log(this.$store.state.userstodo)
    },
    watch:{
        inputData(newVal,oldVal){
            if(newVal.includes("*") || newVal.includes(";")){
                this.inputData = oldVal
            }
        }
    }

}
</script>

<style scoped>
    .input-title{
        font-weight: 600;
        
    }

    h1 {
        /* color: #60a5fa; */
        font-size: 1.5rem;
        font-weight: 700;
        font-family: inherit;
        line-height: 1.1;
        margin-top: 2rem;
    }
    .input-box{
        height: 13%;
    }
      .background {
          width: 50%;
          height: 800px;    
          border-radius: 1rem;
          box-shadow: inset 0 0 10px rgba(8, 8, 8,0.1); 

      }
    .comment-area{

        height: 100vh;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .showlist{
        height: 80%;
        overflow-y: auto;
    }

    @media (min-width: 768px) {
    






    h2{
        margin: 2rem 0 1rem 0;
        font-weight: 900;
        font-size: 2rem;
        
    }
    ul{
        padding: 0;
    }
    }


    @media (max-width:768px) {
        .background {
            width: 99%;
        }

        .input-box{
            height: 10%;
            
        }


        /* h2{

            margin: 2rem 0 1rem 1rem;
            font-weight: 900;
            font-size: 2rem;
        
        }

        .todoinput{
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            height: 150px;
        }
        ul{
           padding: 0;
    }
        .showlist{
            height: 70%;
            overflow-y: auto;
            margin: 1rem 0;
        } */
        /* .suggestTodo {
            display: flex;
            flex-direction: column;
            width:70vw;
            height: 70%;
            background-color:#fff;
            border-radius: 2rem;
            padding: 0 0 0 0;
            border: 2px solid #ccc;
            box-shadow: 0 0 10px rgba(0,0,0,.1);
        }    */
        /* input {
            width: 90%;
            border-radius: 2rem;
            height: 3rem;
            opacity: 1;
            padding-left: 20px;
            margin: auto auto
        }     */
        /* ul {
            height:100%;
            padding: 0 0 0 20px;
            
        }
        label[for="todo"] {
            font-size: 1.3rem;
            font-weight: 600;
            margin:0 0 10px 1rem

            

        }

        .todocontent{
            font-size:30px;
            font-weight: 600;
            display:inline-block;
            width:350px
        }

        .deleteButton{
            font-size:18px;
            border: 2px solid rgb(204, 102, 102);
            border-radius: 12px;
            height: 40px;
            width: 100px;
            font-weight: 600;
        }

        .deleteButton:hover {
            background-color: rgb(204, 102, 102);
        } */




    }



</style>