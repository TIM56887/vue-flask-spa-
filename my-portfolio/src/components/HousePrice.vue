<template>
 <section>
     <h1>新北市房價預測</h1>
    <form action="/process" method="POST">
        <label for="district">選擇地區：</label>
        <select name="district">
            <option value="新莊區">新莊區</option>
            <option value="中和區">中和區</option>
            <option value="汐止區">汐止區</option>
            <option value="土城區">土城區</option>
            <option value="三芝區">三芝區</option>
            <option value="板橋區">板橋區</option>
            <option value="淡水區">淡水區</option>
            <option value="五股區">五股區</option>
            <option value="三重區">三重區</option>
            <option value="林口區">林口區</option>
            <option value="樹林區">樹林區</option>
            <option value="貢寮區">貢寮區</option>
            <option value="新店區">新店區</option>
            <option value="八里區">八里區</option>
            <option value="永和區">永和區</option>
            <option value="泰山區">泰山區</option>
            <option value="三峽區">三峽區</option>
            <option value="鶯歌區">鶯歌區</option>
            <option value="蘆洲區">蘆洲區</option>
            <option value="金山區">金山區</option>
            <option value="深坑區">深坑區</option>
            <option value="萬里區">萬里區</option>
            <option value="雙溪區">雙溪區</option>
            <option value="石門區">石門區</option>
            <option value="瑞芳區">瑞芳區</option>
        </select>
        <label for="land-area">土地總面積平方公尺：</label>
        <input type="number" name="land-area" id="land-area" required>
        <label for="floor">樓層：</label>
        <input type="number" name="floor" id="floor" required>
        <label for="total-floor">建築物總樓層：</label>
        <input type="number" name="total-floor" id="total-floor" required>
        <label for="building-type">建築類型：</label>
        <select name="building-type" id="building-type">
            <option value="公寓(5樓含以下無電梯)">公寓(5樓含以下無電梯)</option>
            <option value="華廈(10層含以下有電梯)">華廈(10層含以下有電梯)</option>
            <option value="住宅大樓(11層含以上有電梯)">住宅大樓(11層含以上有電梯)</option>
            <option value="其他">其他</option>
        </select>
        <label for="years">屋齡：</label>
        <input type="number" name="years" id="years" required>
        <label for="building-area">建物總面積平方公尺：</label>
        <input type="number" name="building-area" id="building-area" required>
        <label for="bedrooms">幾房：</label>
        <input type="number" name="bedrooms" id="bedrooms" required>

        <label for="living-rooms">幾廳：</label>
        <input type="number" name="living-rooms" id="living-rooms" required>

        <label for="bathrooms">幾衛：</label>
        <input type="number" name="bathrooms" id="bathrooms" required>
        <label for="partition">是否有隔間：</label>
        <select name="partition" id="partition">
          <option value="有">有</option>
          <option value="無">無</option>
        </select>
        <label for="manager">是否有管理員：</label>
        <select name="manager" id="manager">
          <option value="有">有</option>
          <option value="無">無</option>
        </select>

        <label for="elevator">是否有電梯：</label>
        <select name="elevator" id="elevator">
          <option value="有">有</option>
          <option value="無">無</option>
        </select>
        <input type="submit" value="提交">
    </form>
    <form action="/">回首頁</form>
 </section>
 
</template>

<script>
export default {

}
</script>

<style scoped>
        h2 {
            font-size:40px;
            text-align:center;
            color:red
        }
        form {
            max-width: 400px;
            margin: 0 auto;
            
        }

        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }

        select,
        input[type="number"] {
            width: 100%;
            padding: 5px;
            margin-bottom: 10px;
        }

        input[type="submit"] {
            background-color: #4CAF50;
            color: white;
            padding: 10px 15px;
            border: none;
            cursor: pointer;
            align-self: center;
            margin-top: 20px;
            width: 100%;
        }
        h1 {
            text-align: center;
        }
</style>