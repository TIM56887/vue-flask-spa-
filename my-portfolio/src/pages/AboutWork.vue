<template>
    <div class="aboutwork">
        <div class="content">
            <P class="title">[2021-3] - [2022-6]遠雄人壽 契約部 </P>
            <p class="text">負責新契約案件審核， 評估新契約風險及與業務員溝通，確保順利完成審核工作。</p>
            <p class="title">[2022-6] - [2023-1]三商美邦人壽 理賠科</p>
            <p class="text">負責理賠案件審查及接待保戶，確保理賠案件完整性和準確性，並與保戶維持良好關係。</p>
            <p class="text"></p>
            <div class="introduce">
            <div class="content1">
                <p class="title">[2023-2] - [2023-6] 參加緯育AI大數據養成班</p>
                <P class="text">今年六月完成了商研院與緯育合作的『AI智慧應用開發實戰班』課程。在這個課程中，我學習到了Python程式設計、MySQL資料庫應用以及資料分析和資料處理等相關技術。</P>
                <h2 class="title">課程內容：</h2>
                <ul class="text"><h4 class="title">MySQL</h4>
                    <li>基本的 SQL 知識：包括對如何使用 SQL 進行數據查詢，如何插入、更新和刪除數據等基本命令的理解。</li>
                    <li>數據庫設計：瞭解如何使用主鍵、外鍵、索引等來優化數據庫性能。</li>
                    <li>一些程式語言的知識：瞭解如何從應用程序（如 Python）連接和操作 MySQL 數據庫。</li>
                </ul>
                <ul class="text"><h4 class="title">Python</h4>
                    <li>Python 基礎知識：基本語法和數據結構。包括變量、數據類型、控制結構（如 if 條件語句、for 和 while 迴圈）、函數和模塊。</li>
                    <li>數據分析套件的理解：如 pandas、NumPy 。使用這些庫進行數據清理、轉換、分析和視覺化。</li>
                    <li>文件操作和數據 I/O：在 Python 中讀寫各種格式的數據文件，例如 CSV、JSON、Excel、SQL 數據庫等。</li>
                    <li>了解機器學習：Tensorflow、Scikit-learn 等機器學習庫實際使用經驗。</li>
                </ul>
            </div>
            <div class="picDiv">
                <a  href="https://www.tibame.com/goodjob/AI_tp">
                    <img class="pic" src="../assets/aboutlearnpic.jpeg" alt="learningPicture">
                </a>
            </div>
        </div>
        </div>
    </div>
</template>

<script>
export default {

}
</script>

<style scoped>
    @media (min-width:768px){
    .introduce {
        width: 100%;
        display: flex;
        flex-direction: row;
    }
    .content1{
        width:70%;
        margin-top: 2rem;
        margin-right: 2rem;
        
    }
        .pic{
        max-width:100%;
        max-height:300px;
        border-radius: 10px;
        /* margin-top:60px ; */
        /* object-fit: fill; */
        
        }
        .picDiv {
        width: 30%;
        height: 450px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
        .aboutwork{
            width:100%;
            
        }
        .content{
            margin-top: 2rem;
        }
        p{
            font-size: 1.5rem;
            
        }

        .title{
            
            font-size: 1.8rem;
            font-weight: 400;
            color: #1e1e1e;
        }

        .text {
            padding: 0 0 0 20px;
            font-weight: 300;
            color:#616161;
            font-size:1.3rem;
        }
    }
    @media (max-width:768px){
        .picDiv {
        width: 100%;
        height: 300px;
        display: flex;
        align-items: center;
        justify-content: center;
        }
        .pic{
        max-width:100%;
        max-height:300px;
        border-radius: 10px;
        /* margin-top:60px ; */
        /* object-fit: fill; */
        
    }
        .aboutwork{
            width:100%;
            
        }
        .content{
            margin: 0rem;
        }
        

        .title{
            font-size: 1.5rem;
            font-weight: 700;
            color: #1e1e1e;
        }

        .text {
            font-size: 1.2rem;
            padding: 0 0 0 10px;
            font-weight: 400;
            margin: 1rem 0;
            color:#616161;
        }
    }
    
</style>