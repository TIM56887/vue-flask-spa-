<template>
 <section class="d-flex justify-content-center flex-column align-items-center">
    <div class="main mt-5" style="min-width: 800px;">
        <div class="title">
            <h1>新北市房價預測系統</h1>
        </div>
            <label for="district">選擇地區：</label>
            <select name="district" v-model="form.district">
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
            <label for="land-area" >土地總面積平方公尺：</label>
            <input type="number" min="0" name="land-area" id="land-area" required v-model="form.landArea">
            <label for="floor">樓層：</label>
            <input type="number" min="0" name="floor" id="floor" required v-model="form.floor">
            <label for="total-floor">建築物總樓層：</label>
            <input type="number" min="1" name="total-floor" id="total-floor" required v-model="form.totalFloor">
            <label for="building-type">建築類型：</label>
            <select name="building-type" id="building-type" v-model="form.buildingType">
                <option value="公寓(5樓含以下無電梯)">公寓(5樓含以下無電梯)</option>
                <option value="華廈(10層含以下有電梯)">華廈(10層含以下有電梯)</option>
                <option value="住宅大樓(11層含以上有電梯)">住宅大樓(11層含以上有電梯)</option>
                <option value="其他">其他</option>
            </select>
            <label for="years">屋齡：</label>
            <input type="number" min="0" name="years" id="years" required v-model="form.years">
            <label for="building-area" >建物總面積平方公尺：</label>
            <input type="number" min="1" name="building-area" id="building-area" required v-model="form.buildingArea">
            <label for="bedrooms">幾房：</label>
            <input type="number" min="0" name="bedrooms" id="bedrooms" required v-model="form.bedrooms">

            <label for="living-rooms">幾廳：</label>
            <input type="number" min="0" name="living-rooms" id="living-rooms" required v-model="form.livingRooms">

            <label for="bathrooms">幾衛：</label>
            <input type="number" min="0" name="bathrooms" id="bathrooms" required v-model="form.bathrooms">
            <label for="partition">是否有隔間：</label>
            <select name="partition" id="partition" v-model="form.partition">
            <option value="有">有</option>
            <option value="無">無</option>
            </select>
            <label for="manager">是否有管理員：</label>
            <select name="manager" id="manager" v-model="form.manager">
            <option value="有">有</option>
            <option value="無">無</option>
            </select>

            <label for="elevator">是否有電梯：</label>
            <select name="elevator" id="elevator" v-model="form.elevator">
            <option value="有">有</option>
            <option value="無">無</option>
            </select>
            <div class="but d-flex justify-content-center align-items-center" style="height: 100px;">
                <button @click="submitData" class="w-25 fs-3 btn btn-outline-secondary">提交</button>
            </div>
            
    </div>
    <div 
        class="position-fixed top-50 start-50 translate-middle border pt-4 bg-white rounded-3 border-dark-subtle z-3"
        v-if="fetching || predicted"
    >   
        <div v-if="fetching" class="box d-flex flex-column justify-content-center">
            <h2 class="text-center">Loading <span>{{ loadingAnimation }}</span></h2>
        </div>
        <div v-if="predicted || !fetching" class="box d-flex flex-column justify-content-between align-item-center" >
            <h2 class="text-center fs-1 fw-bold">預測價格</h2>
            <h1>{{ predictPrice }}</h1>
            <button type="button" class="btn btn-light" @click="predicted = false">Close</button>
        </div>
    </div>
    <div v-if="predicted || fetching" class="overlay" @click="predicted = false"></div>
    <button
        @click="goPreview" 
        type="button" class="btn btn-outline-secondary position-fixed bottom-0 start-0 fs-4 m-4"><i class="bi bi-chevron-double-left"></i>介紹</button>
 </section>
    
    
 
</template>

<script>
import axios from 'axios'

export default {
    data(){
        return{
            form: {
                district: '',
                landArea: '',
                floor: '',
                totalFloor: '',
                buildingType: '',
                years: '',
                buildingArea: '',
                bedrooms: '',
                livingRooms: '',
                bathrooms: '',
                partition: '',
                manager: '',
                elevator: '',
            },
            fetching: false,
            predictPrice: 0,
            predicted:false,
            loadingAnimation:"."
        }

    },
    methods:{
        submitData(){
            this.predicted = false; 
            if (this.hasEmptyValue(this.form)){
                alert('please fill in all fields')
            }else {
                this.fetching = true;
                axios.post('/process',this.form)
                .then(res => {
                    const intervalId = setInterval(() => this.loadingAnimationRun(), 500);
                    setTimeout(()=>{
                        this.predictPrice = res.data.price
                    this.fetching = false
                    this.predicted = true
                    clearInterval(intervalId);
                    },3000)
                    
                })
                .catch(err => {
                    console.log(err)
                    this.fetching = false;
                })
            }
        },
        hasEmptyValue(obj){
            for (const key in obj){
                if(Object.prototype.hasOwnProperty.call(obj, key)){
                    if(obj[key] === ''){
                        return true;
                    }
                }
            }
            return false;
        },
        scrollToTop(){
                window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        },
        loadingAnimationRun(){
            if(this.loadingAnimation.length < 3){
                this.loadingAnimation += '.';
            }else{
                this.loadingAnimation = '';
            }
            
        },
        goPreview(){
            this.$emit('changePage')
        }
    }

}
</script>

<style scoped>
        .overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.5);
            
        }
        .box {
            width: 350px;
            height: 300px;
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