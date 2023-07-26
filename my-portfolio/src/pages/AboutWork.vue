<template>
    <div class="aboutwork">
        <div class="content">
            <P class="title">[2021-3] - [2022-6]遠雄人壽 契約部 </P>
            <p class="text">負責新契約案件審核， 評估新契約風險及與業務員溝通，確保順利完成審核工作。</p>
            <p class="title">[2022-6] - [2023-1]三商美邦人壽 理賠科</p>
            <p class="text">負責理賠案件審查及接待保戶，確保理賠案件完整性和準確性，並與保戶維持良好關係。</p>
            <p class="text"></p>
        </div>
    </div>
</template>

<script>
export default {

}
</script>

<style scoped>
    @media (min-width:768px){
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