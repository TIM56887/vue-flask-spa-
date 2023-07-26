<template>
  <section class="todoapp">
    
    <div class="todo">
      <MyTodo />
      <SuggestTodo />
    </div>
  </section>

</template>

<script>
import MyTodo from './MyTodo.vue'
import SuggestTodo from './SuggestTodo.vue'
export default {
  components:{
    MyTodo,
    SuggestTodo
  }
}
</script>

<style scoped>

    



  @media (min-width: 768px) {

    
    .todoapp{
      height: 90vh;
      background-color: #ffffff;
      padding-top: 1rem;
    }
      .todo {
      display: flex;
      height: 80vh;
      justify-content: space-evenly;
      padding: 5vh 0 0 0;
    }  


    h1{
      display: flex;
      justify-content: center;
      color: rgb(51, 31, 5);
      
    }
    .todoh1{
        display: inline;
        text-align: center;
        height: 5vh;
        padding-bottom: 4rem;
        border-bottom: 5px solid rgb(59, 35, 3);
    }
    .todoh1{
      text-align: center;
      height: 5vh;
      font-size: 3rem;
      font-weight: 700;
    }
  }

  @media (max-width:768px) {
    .todo {
    display: flex;
    flex-direction: column;
    height: 100vh;
    justify-content: center;
    align-items: center;
    padding: 10px 0 0 0;
  }  
  .todoh1{
        text-align: center;
        height: 5vh;
        padding-bottom: 0px;
        border-bottom: 5px solid rgb(110, 66, 8);
    }
    h1{
      display: flex;
      justify-content: center;
      margin-top:0;
    }
    .todoapp{
      padding-top: 1rem;
      background-color: #ffffff;
    }

  }
  
</style>