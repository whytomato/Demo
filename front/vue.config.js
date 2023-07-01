// vue.config.js
module.exports = {
    devServer: {
        proxy: {
            '/api': {
                target: 'http://127.0.0.1:8000',  // 后端接口的地址
                changeOrigin: true,
                pathRewrite: {
                    '^/api': '/api'  // 如果后端接口的路径有前缀，可以在此进行重写
                }
            }
        }
    }
}
