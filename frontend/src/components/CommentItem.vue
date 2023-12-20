<template>
    <li class="container-fluid pb-1 px-0 px-md-4 border-bottom mt-4">
        <div class="row">
            <div class="col-md-1 col-2 overflow-hidden  d-flex justify-content-end p-md-0">
                <img :src="comment.pictureUrl" alt="pf" class="object-fit-fill border rounded-circle">
            </div>
            <div class="col-md-11 col-10">
                <div class="container">
                    <div class="row justify-content-between">
                        <div class="col-2 p-0">
                            <div class="user fw-semibold">
                                {{ comment.displayName }}
                            </div>
                        </div>
                        <div class="col-3 p-0 text-secondary time text-end">
                            {{ comment.commentDate.slice(0,17).replace("T"," ") }}
                        </div>
                    </div>
                    <div v-show="!isEditing" class="row textArea">
                        <pre class="p-0 px-md-1">{{ comment.commentText }}</pre>
                    </div>
                    <div v-show="isEditing" class="row textArea">
                        <textarea 
                            ref="editingInput" 
                            cols="30" rows="5" 
                            v-model="editingvalue"
                            @blur="doneEdit"
                            ></textarea>
                    </div>
                    <div class="row justify-content-end bottom-row ">
                        <div  v-if="!isEditing && currentUser === comment.userId" @click="editComment" class="col-1 text-end p-0">                            
                            <i class="bi bi-pencil-square editicon align-middle p-1"></i>
                        </div>
                        <div v-if="!isEditing && currentUser === comment.userId" @click="deleteComment" class="col-1 p-0 ms-2">
                            <i class="bi bi-trash3 deleteicon align-middle p-1"></i>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </li>
</template>

<script>
export default {
    name:'CommentItem',
    props:['comment','currentUser'],
    data(){
        return{
            isEditing:false,
            editingvalue:""
        }
    },
    methods:{
        editComment() {
            this.isEditing = !this.isEditing;
            this.editingvalue = this.comment.commentText;
            this.$nextTick(() => {
                this.$refs.editingInput.focus();
            });
        },
        doneEdit(){
            this.isEditing = false;
            if (this.comment.commentText !== this.editingvalue){
                this.sendEditedComment()
            }
            
        },
        sendEditedComment(){
            const updateComment = {
                commentId: this.comment.commentId,
                newValue: this.editingvalue
            }
            this.$store.dispatch('updateComment',updateComment)            
        },
        deleteComment(){
            const id = {commentId:this.comment.commentId}
            this.$store.dispatch('deleteComment',id)
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