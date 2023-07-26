<template>
    <li class="todoli d-flex flex-row justify-content-center">
        <div class="content shadow p-1 mb-3 bg-body-tertiary rounded">
            <div class="tododate">{{ todo.date }}</div>
            
            <div v-show="!isEditing" class="todocontent">{{ todo.task }}</div>
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
            </div>
            
           
        </div>
    </li>
</template>

<script>
export default {
    name:'SuggestTodoItem',
    props:['todo'],
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
    .deleteicon{
        font-size: 1.5rem;
        transition: all 0.1s;
        
    }
    .deleteButton:hover .deleteicon{
        color: rgb(192, 18, 18);
        font-size: 1.8rem;
    }
    .editicon {
        font-size: 1.5rem;
        transition: all 0.1s;
    }

    .editButton:hover .editicon{
        color: green;
        font-size:1.8rem;
    }
    .editButton{
        width:11%;
        background: transparent;
        display: flex;
        justify-content: center;
        align-items: center;
        margin-right: 0;
        height: 80%;
    }

    .editButton:hover{
        background: rgba(0, 0, 0, 0.1);
        border-radius: 0.9rem;
    }

    .content{
        align-items: center;
        display:flex;
        width: 90%;
        height: 60px;
        background-color: #ebedf0;
        border-radius: 1rem;
    }

    .tododate{
        width:29%;
        font-size: 1.5rem;
        font-weight: 700;
        text-align: center;
    }
    .todocontent{
        width:50%;
        overflow-x:auto;
        
    }
    .deleteButton{
        width:11%;
        background: transparent;
        display: flex;
        justify-content: center;
        align-items: center;
        margin-right: 5px;
        height: 80%;
    }
    .deleteButton:hover{
        background: rgba(0, 0, 0, 0.1);
        border-radius: 0.9rem;
    }

    .todoli{
        list-style-type: none;
        margin-bottom: 1rem;
    }


    /* fds-blue-05: #ECF3FF;
    --fds-blue-30: #AAC9FF;
    --fds-blue-40: #77A7FF;
    --fds-blue-60: #1877F2;
    --fds-blue-70: #2851A3;
    --fds-blue-80: #1D3C78;
    --fds-button-text: #444950; */
</style>