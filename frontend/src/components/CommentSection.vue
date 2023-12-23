<template>
    <section class="comment-area">       
        <div class="mt-5  area container-sm ">
            <div class="row p-0">
                <h1><div class="text-center fs-3">Comment . . .</div></h1>
            </div>
            <div class="suggestTodo h-100 row ">
                <div class="showlist mt-4 h-75">
                    <ul>
                        <CommentItem v-for="comment in comments" :key="comment.commentId" :comment="comment" :currentUser="currentUserData.userId"/>
                    </ul>
                </div>
                <div v-if="isLoggedIn" class="d-flex justify-content-center input-box">
                    <div class="input-group input-group-lg shadow-sm mx-5 bg-body-tertiary rounded" >
                        <textarea
                            type="text" 
                            class="form-control fs-5 " 
                            aria-label="Sizing example input" 
                            aria-describedby="inputGroup-sizing-lg"
                            placeholder="your input is always good . . ." 
                            maxlength="100"
                            v-model="inputData"
                        ></textarea>
                        <button @click="addNewComment"><span class="input-group-text input-title" id="inputGroup-sizing-lg"><i class="bi bi-send fs-4"></i></span></button>
                    </div>
                </div>
            </div>
            <button v-if="!isLoggedIn" type="button" class="btn btn-success sticky-bottom" @click="liffLogin">
                <i class="bi bi-line mx-3 fs-3"></i>
                <span class="me-2 fs-5 lh-lg fw-semibold">Login to comment</span>
            </button>
        </div>
        
        
    </section>
</template>

<script>
import liff from "@line/liff";
import { mapState } from 'vuex'
import CommentItem from './CommentItem.vue';
export default {
    name:'CommentSection',
    components:{
        CommentItem
    },
    data() {
        return {
            user:'',
            inputData:'',
            currentUserData:{},
            isLoggedIn:false
        };
    },
    methods:{
        liffLogin() {
            liff.init({liffId:'2000362113-Dd5JOa2e'})
            .then(()=> {
                if (!liff.isLoggedIn()) {
                    liff.login();
                }
            })
            .catch((err) => {
                this.message = "LIFF init failed.";
                this.error = `${err}`;
            });
        },
        addNewComment() {
            if (this.inputData) {
                let commentData = {
                    ...this.currentUserData,
                    commentDate: new Date().toLocaleString("zh-TW", { timeZone: "Asia/Taipei" }),
                    commentText: this.inputData
                };
                this.$store.dispatch('sendComment',commentData);
                this.inputData = "";
            }
        }
    },
    computed:{
        ...mapState(['comments']),
    },
    mounted(){
        liff.init({liffId:'2000362113-Dd5JOa2e'})
        .then(() => {
            if (liff.isLoggedIn()) {
                    this.isLoggedIn = true
                    liff.getProfile()
                    .then((pf) => {
                        this.isLoggedIn = true
                        this.currentUserData = pf
                    })
                    .catch((err) => {
                        console.log("error",err)
                    })
                }
        });
        this.$store.dispatch('getComment');
    },
    watch:{
        inputData(newVal,oldVal){
            if(newVal.includes("*") || newVal.includes(";") || newVal.includes("'")){
                this.inputData = oldVal;
            }
        }
    }

}
</script>

<style scoped>
    
    button {
        border: none;
    }
    .area {
        max-width: 680px;
    }
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
          width: 60%;
          height: 800px;    
          border-radius: 1rem;
          box-shadow: inset 0 0 10px rgba(8, 8, 8,0.1); 

      }
    .comment-area{
        min-height: 100vh;
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