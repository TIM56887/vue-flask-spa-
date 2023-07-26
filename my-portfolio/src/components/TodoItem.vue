<template>
  <li class="todoli">
  
    <div class="createDate">
      {{ todo.date }}
    </div>
    <div class="content">
      {{ todo.content }}
    </div>
    
      
  </li>
</template>

<script>
export default {
  name:'TodoItem',
  props:['todo']

}
</script>

<style scoped>
  @media (min-width: 768px){
    .metaTodo{
      display: flex;
      width: 500px;
      
    }
    .createDate {
      display: inline-block;
      font-size: 2rem;
      font-weight: 800;
      width: 100px;
      
    }  

    .content{
      display: inline-block;
      font-size: 1.8rem;
      font-weight: 700;
      width:300px;
    }

    .daySpent {
      display: inline-block;
      width:200px;
      text-align:center;
      font-weight: 600;
      
    }

    .todoli {
      display: flex;
      align-items: center;
      list-style-type: none;
      margin: 20px 0 0 0;
      padding:0;
      list-style-type: none;
    }
  }

  @media (max-width: 768px) {
    .createDate {
      display: inline-block;
      font-size: 1.3rem;
      font-weight: 600;
      width: 40px;
      margin-right: 20px;
      }  

    .content{
      display: inline-block;
      font-size: 1.2rem;
      font-weight: 600;
      width:300px;
    }  

    .todoli {
      margin: 5px 0 0 -10px;
      list-style-type: circle;
      display: flex;
      align-items: center;
  }
    


  }
  
</style>