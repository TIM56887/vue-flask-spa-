<template>
<nav class="navbar">
    <div class="container-fluid">
        <div class="d-flex w-100 justify-content-between align-items-center">
            <div class="ps-4 ">
                <h1 class="fs-4 lh-lg m-0"><a href="" class="text-decoration-none fw-bold text-secondary">TIM</a></h1>
            </div>
            <div class=""> 
                <ul class="w-100 d-flex lh-lg fs-4 text-center text-nowrap menu justify-content-center m-0 position-relative" >
                    <li class="px-5 rounded" @click="scrollTo('section1')">Project</li>
                    <li class="px-5 rounded" @click="scrollTo('section2')">Resources</li>
                    <li class="px-5 rounded" @click="scrollTo('section3')">About me</li>
                    <li class="currentLine" :style="{left: leftpx + 'px'}" :class="{'d-none':hideLine }"></li>
                </ul>
            </div>
            <div class="hamburger">
                <button class="navbar-toggler" type="button" @click="showMenu" >
                    <span class="navbar-toggler-icon"></span>
                </button>
            </div>
        </div>
    </div>
    <ul class="menu-phone fs-3 text-secondary-emphasis rounded-3" v-if="isVisible">
        <li class="rounded-3" @click="scrollTo('section1')">Project</li>
        <li class="rounded-3" @click="scrollTo('section2')">Resources</li>
        <li class="rounded-3" @click="scrollTo('section3')">About me</li>
    </ul>
</nav>
</template>

<script>
    export default {
        data(){
            return{
                isVisible:false,
                scrollPosition: 0,
                leftpx:85,
                hideLine: true
            }
        },
        methods: {
            async scrollTo(sectionId) {           
                if (this.$route.path !== '/') {
                    await this.$router.push('/');
                }
                this.$nextTick(() => {
                    const el = document.getElementById(sectionId);
                    if (el) {
                        el.scrollIntoView({ behavior: 'smooth' });
                        this.isVisible = false;
                    }
                });
            },
             showMenu(){
                this.isVisible = !this.isVisible;
            },
            updateScroll(){
                this.scrollPosition = window.scrollY;
            }
        },
        mounted() {
            window.addEventListener("scroll",this.updateScroll)
        },
        beforeDestroy(){
            window.removeEventListener("scroll",this.updateScroll)
        },
        computed:{
            section1Position(){
                return document.getElementById("section1").offsetTop - 200
            },
            section2Position(){
                return document.getElementById("section2").offsetTop -200
            },
            section3Position(){
                return document.getElementById("section3").offsetTop - 600
            },
        },
        watch:{
            scrollPosition(newVal){
                console.log(newVal,this.section1Position,this.section2Position,this.section3Position)
                console.log(newVal < this.section1Position)
                if(newVal > this.section1Position && newVal < this.section2Position ) {
                    this.hideLine = false;
                    this.leftpx = 85;
                }else if(newVal > this.section2Position && newVal < this.section3Position){
                    this.hideLine = false;
                    this.leftpx = 280;
                } else if(newVal > this.section3Position){
                    this.hideLine = false;
                    this.leftpx = 485;
                }else{
                    this.hideLine = true;
                }
            }
        }


    }
</script>

<style scoped>
.currentLine{
    position: absolute;
    bottom: 0px;
    height: 4px;
    width: 64px;
    background-color: #1e1e1e;
    padding: 0;
    transition: all .2s ease-in-out;
}
.active {
  border-bottom: 2px solid #000; 
}
.hamburger {
    visibility: hidden;
}
.navbar{
    border-bottom: 0px solid rgb(175, 175, 175);
    box-shadow: 0 1px 0 0 rgba(0,0,0,.1);
    opacity: .95;
    position: fixed;
    width: 100%;
    height: 75px;
    background: #fff;
    z-index: 1001;
}
li:hover {
  cursor: pointer; 
  background-color: #f5f5f5; 
}
.menu {
    list-style-type: none;
}
.menu-phone {
    list-style-type: none;
    background-color: #fff;
    width: 100vw;
    position: fixed;
    top: 76px;
    border-radius: 4px;
    padding: 0;
    text-indent: 20px;
    z-index: 1000;
}
@media (max-width: 768px) {
    .menu {
        display: none !important;
        
    }

    .hamburger {
        visibility: visible;
    }

    .menu-phone li {
        border: 0px solid rgb(175, 175, 175);
        box-shadow: 0 1px 0 0 rgba(0,0,0,.1);
        line-height: 2;
    }
}

</style>