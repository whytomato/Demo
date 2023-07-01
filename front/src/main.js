import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

// 引入 Element Plus 组件
import ElementPlus from 'element-plus'

createApp(App).use(store).use(router).use(ElementPlus).mount('#app') // 在这里使用 Element Plus
