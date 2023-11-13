<template>
      <div class="aboutlife">
        <div class="content">
            <p>Location：台北、桃園</p>
            <p>Contact：0965458387</p>
            <p>E-mail：timmy56887@icloud.com</p>
        </div>
        <div class="Picborder">
            <div class="picBox">
                <img class="linePIC" src="../assets/lineimg.jpeg" alt="lineQRcode">
                <div class="middle">
                    <div class="text">ID:timmy56887</div>
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
    

    

    
    @media (max-width:768px) {
    .picBox {
        position: relative;
        width: 100%;
        height: 100%;
    }
    .picBox:hover .linePIC {
        opacity: 0.3;
    }
    .picBox:hover .middle {
        opacity: 1;
    }
    .linePIC{
        max-width: 200px;   
        max-height: 300px;
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
    }
    .Picborder {
        height: 300px;
    }

    .linePIC {
        opacity: 1;
        width: 50%;
        height: auto;
        transition: .5s ease;
        backface-visibility: hidden;
    }

    .middle {
        transition: .5s ease;
        opacity: 0;
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        -ms-transform: translate(-50%, -50%);
        
    }


    .text {
        background-color: #4CAF50;
        color: white;
        font-size: 0.8rem;
        padding: 16px 32px;
    }
    .content{
        margin-top: 2rem;
        color:#1e1e1e;
    }

    
    p{
        font-size: 1.5rem;
        font-weight: 600;
    }
    .aboutlife {
        width:100%;
        padding:0.5rem 0 0 0;
        display: flex;
        justify-content: center;
        flex-direction: column;
    }

    .title{
        font-weight: 900;
    }
    }
    @media (min-width:768px) {
        .picBox {
            position: relative;
            width: 100%;
            height: 100%;
        }
        .picBox:hover .linePIC {
            opacity: 0.3;
        }
        .picBox:hover .middle {
            opacity: 1;
        }
        .linePIC{
            opacity: 1;
            display: block;
            width: 50%;
            height: auto;
            transition: .5s ease;
            max-width: 200px;   
            max-height: 300px;
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            display: block;
            backface-visibility: hidden;
        }
        .Picborder {
            width:25%;
        }
        .middle {
            transition: .5s ease;
            opacity: 0;
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            -ms-transform: translate(-50%, -50%);
        }

        .text {
            background-color: #4CAF50;
            color: white;
            font-size: 0.8rem;
            padding: 16px 32px;
        }


        .content{
            margin-top: 2rem;
            color:#1e1e1e;
            width:41%
        }
        p{
            font-size: 1.9rem;
            font-weight: 900;
        }
        .aboutlife {
            width:100%;
            padding:0.5rem 0 0 0;
            display: flex;
            justify-content: center;
        }
    }
</style>