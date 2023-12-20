import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
Vue.use(Vuex)
const actions = {
    sendComment(context,value){
        axios.post('/sendcomment',value).then(
            error => {
                console.log('請求失敗',error.message)
            }
        )
        context.dispatch('getComment')

    },
    getComment(context){
        axios.get('/getcomment').then(
            response =>{
                context.commit('GETCOMMENT',response.data)
            },
            error => {
                console.log('請求失敗',error.message)
            }
        )
    },
    updateComment(context, value){
        console.log(value)
        axios.post('/updatecomment',value).then(
            response => console.log(response)
        );
        context.commit('UPDATECOMMENT', value)
        
    },
    deleteComment(context, value){
        axios.post('/deletecomment', value)
        .then(
            res => {
                console.log(res);
                context.commit('DELETECOMMENT',value.commentId)
            }
            
        )
    }
}

const mutations = {
    SENDCOMMENT(state, value){
        state.comments.push(value)
    },
    GETCOMMENT(state,value){
        state.comments = value
    },
    UPDATECOMMENT(state,value){
        let targetComment = state.comments.find( comment => comment.commentId === value.commentId)
        targetComment.commentText = value.newValue
    },
    DELETECOMMENT(state,value){
        let index = state.comments.findIndex(comment => comment.commentId === value)
        console.log(index)
        state.comments.splice(index, 1)
    }
}

const state = {
    todo:[],
    userstodo:[],
    comments:[]
}


const store = new Vuex.Store({
    actions,
    mutations,
    state
})

export default store