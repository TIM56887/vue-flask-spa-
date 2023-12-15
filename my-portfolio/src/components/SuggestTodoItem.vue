<template>
    <li class="container-fluid pb-1 px-0 border-bottom mt-4">
        <div class="row">
            <div class="col-1 overflow-hidden ps-4 d-flex justify-content-end p-0">
                <img :src="comment.pictureUrl" alt="pf" class="object-fit-fill border rounded-circle">
            </div>
            <div class="col-11">
                <div class="container">
                    <div class="row justify-content-between">
                        <div class="col-2 p-0">
                            <div class="user fw-semibold">
                                {{ comment.displayName }}
                            </div>
                        </div>
                        <div class="col-3 p-0 text-secondary time text-end">
                            {{ comment.commentDate.slice(0,16).replace("T"," ") }}
                            
                        </div>
                    </div>
                    <div class="row textArea">
                        <pre class="comment ps-1">
                                {{ comment.commentText }}
                        </pre>
                    </div>
                    <div class="row justify-content-end bottom-row ">
                        <div v-if="currentUser === comment.userId" class="col-1 text-end p-0">                            
                            <i class="bi bi-pencil-square editicon align-middle p-1"></i>
                        </div>
                        <div v-if="currentUser === comment.userId" class="col-1 p-0 ms-2">
                            <i class="bi bi-trash3 deleteicon align-middle p-1"></i>
                        </div>
                        
                    </div>
                </div>
            </div>
            

            <div>
                
            </div>
            <!-- <div v-show="!isEditing" class="todocontent">{{ todo.task }}</div>
            <input ref="editingInput" 
                    v-show="isEditing" 
                    v-model="editingvalue" 
                    @blur="sendeditedtodo($event,todo)" 
                    class="todocontent" >
            <div v-if="$store.state.userstodo.includes(todo.id)" class="editButton" @click="edittodo(todo)">

                <i class="bi bi-pencil-square editicon"></i>
            </div>
            <div v-if="$store.state.userstodo.includes(todo.id)" class="deleteButton" @click="deletetodo(todo.id)">   
                <i class="bi bi-trash3 deleteicon"></i>
            </div> -->
            
           
        </div>
    </li>
</template>

<script>
export default {
    name:'SuggestTodoItem',
    props:['comment','currentUser'],
    data(){
        return{
            isEditing:false,
            editingvalue:""
        }
    },
    methods:{
        deletetodo(id){
            
            this.$store.dispatch('deletetodo',id)
        },
        edittodo(todo){
            this.isEditing = !this.isEditing
            this.editingvalue = todo.task
            this.$nextTick(() => {
                this.$refs.editingInput.focus();
            });
        },
        sendeditedtodo(e,todo){
            if (todo.task !== e.target.value){
                let content = e.target.value
                let id = todo.id
                this.isEditing=false
                this.$store.dispatch('edittodo',{content,id})
            }
            this.isEditing=false
        }
    }

}
</script>

<style scoped>
    img {
        height: 50px;
    }
    li {
        min-height: 130px;
        list-style-type: none;
    }
    .time {
        font-size: 14px;
    }
    .textArea {
        min-height: 90px;
    }
    .deleteicon:hover{
        background: rgba(0, 0, 0, 0.1);
        border-radius: 0.9rem;
        font-size: 20px;
        color: rgb(239 68 68);
    }
    .editicon:hover{
        background: rgba(0, 0, 0, 0.1);
        border-radius: 0.9rem;
        font-size: 20px;
        color: rgb(5 150 105);
    }
    .bottom-row {
        height: 30px;
    }
    
</style>