import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import 'sweetalert2/dist/sweetalert2.css'
import * as ElementPlusIconsVue from '@element-plus/icons-vue'
import axios from 'axios';

axios.defaults.baseURL = 'http://43.138.116.210';

const app = createApp(App)

// 全局注册 Element Plus 组件
app.use(ElementPlus)

// 全局注册 Element Plus 图标组件
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
    app.component(key, component)
}

// 使用路由和状态管理
app.use(router).use(store)

// 挂载到页面
app.mount('#app')
