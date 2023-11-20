import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
Vue.use(Vuex)
const actions = {
    SendTodo(context,value){
        axios.post('/addtodo',value).then(
            response =>{
                console.log('請求成功了',response.data)
                localStorage.setItem('userId', response.data.userid);
                context.state.userstodo.push(response.data.contentid)
                context.dispatch('gettodo')
            },
            error => {
                console.log('請求失敗',error.message)
            }
        )
        
    },
    gettodo(context){
        axios.get('/todo').then(
            response =>{
                
                context.commit('GETTODO',response.data)
            },
            error => {
                console.log('請求失敗',error.message)
            }
        )
    },
    deletetodo(context,id){
        axios.post('/deletetodo',{'id': id}).then(
            response =>{
                console.log('請求成功',response.data)
                context.dispatch('gettodo')
            },
            error => {
                console.log('請求失敗了',error.message)
            }
        )
    },
    edittodo(context,value) {
        console.log(value)
        axios.post('/editTodo',value).then(
            response =>{
                console.log('請求成功',response.data)
                context.commit('EDITTODO',value)
            },
            error => {
                console.log('哇靠!請求失敗了',error.message)
            }
        )
    },
    getusertodo(context,userid){
        axios.post('/getUserTodo',{'userid':userid}).then(
            response =>{
                
                const userstodo = response.data.map(function(item) {
                    return item.id;
                })
                context.commit('GETUSERTODO',userstodo)

            },
            error => {
                console.log('請求失敗',error.message)
            }
        )
    }
}

const mutations = {
    SENDTODO(state,value){
        state.todo.push(value)
    },
    GETTODO(state,value){
        state.todo=value
    },
    GETUSERTODO(state,value){
        Vue.set(state, 'userstodo', value);
    },
    EDITTODO(state,value){
        let obj = state.todo.find(item => item.id === value.id);
        obj.task =  value.content
    }
    
}

const state = {
    todo:[],
    userstodo:[],
    
}


const store = new Vuex.Store({
    actions,
    mutations,
    state
})

export default store