<template>
    <!-- <div class="card-wrapper">
    <div class="card" >
        <div class="content1"><div class="card-title">新建团队</div></div>
        <div class="content2"><div class="card-description">description</div></div>
        
      </div>
    </div>

    <div class="group_card">

    </div>


    <div class="container">
            <div class="button-wrapper">
                <svg width="160" height="60">
                    <rect class="rectangle" ></rect>
                </svg>
                <div class="btn">按钮</div>
            </div>
        </div> -->









        <div class="center-container">
  <div class="center-box">
    <div class="box1">
        <div class="box2">
            <div class="box3"></div>
        </div>
        
    </div>
    
  </div>
  
</div>
  </template>
  
  


  
  <style scoped>

  .card-wrapper {
    /* 开启3D空间 */
    perspective: 300px;
}

.card {
    /* 基础布局 */
    width: 180px;
    height: 180px;
    margin: 4px;
    font-size: 48px;
    position: relative;
    text-align: center;

    /* 翻转特效时间 */
    transition: transform 0.8s;
    /* 保留3D空间 */
    transform-style: preserve-3d;
    /* background: linear-gradient(45deg, #3498db, #9b59b6); */
    border-radius: 10px;
    
}


.content1,
.content2 {
    position: absolute;
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    /* 隐藏3D的背面 */
    backface-visibility: hidden;
    border: 1px solid #d2dae2;
    color: black;
    background: linear-gradient(45deg, #30e591, #388bc6);
    border-radius: 10px;
}

/* 翻转卡片 */
.content2 {
    transform: rotateY(180deg);
}

.card-wrapper:hover .card{
    transform: rotateY(180deg);
}
.group_card{
    /* background-color: pink; */
    height: 100px;
    width:160px;
    border-radius: 12%;
    transition: 0.4s ease-in-out;
    box-shadow: 0 0 10px 2px rgb(163, 163, 163);
}

.group_card:hover{
transform: translate(-5px,-5px);
box-shadow: 4px 4px 6px 3px gray;
}

.container {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 160px;
    height: 60px;
    background: pink;
    box-shadow: 0 0 10px 2px rgb(163, 163, 163);;
}

.button-wrapper {
    position: relative;
    width: 160px;
    height: 60px;
    text-align: center;
}

.rectangle {
    width: 160px;
    height: 60px;
    stroke-width: 8px;
    stroke: #ff6348;
    fill: transparent;
    stroke-dasharray: 100 500;
    stroke-dashoffset: -254;
}
.btn {
    color: black;
    font-size: 18px;
    letter-spacing: 6px;
    position: relative;
    top: -48px;
}

@keyframes extend {
    to {
        stroke-dasharray: 440;
        stroke-dashoffset: 0;
        stroke-width: 2;
    }
}

.button-wrapper:hover .rectangle {
    animation: 0.5s extend linear forwards;
}








.center-container {
  display: flex;
  justify-content: center; /* 水平居中 */
  align-items: center; /* 垂直居中 */
    height: 100vh; }

.center-box {
  width: 700px; /* 设置盒子的宽度 */
  height: 400px; /* 设置盒子的高度 */
  background-color: #f0f0f0; /* 设置背景颜色 */
}
.box1{
    width: 100%;
    height: 35%;
    background-color: pink;
}
.box2{
    display: flex;
    height: 100%;
    width:20%;
    background-color: blue;
    margin-left: 5%;
    justify-content: center; /* 水平居中 */
  align-items: center; /* 垂直居中 */
}
.box3{
    height: 80%;
    width: 80%;
    background-color: green;
    border-radius: 50%;

}
</style>
  