// 工具类模块
refresh_token_url = api_domain + '/api/v1/auth/refresh'
upload_file_url = api_domain + '/api/v1/upload/'
batch_upload_file_url = api_domain + '/api/v1/upload/batch'

// 字符串格式化方法
String.prototype.format = function (args) {
    let result = this;
    if (arguments.length < 1) {
        return result;
    }
    let data = arguments;		// 如果模板参数是数组
    if (arguments.length === 1 && typeof (args) == "object") {
        //如果模板参数是对象
        data = args;
    }
    for (let key in data) {
        let value = data[key];
        if (undefined !== value) {
            result = result.replace("{" + key + "}", value);
        }
    }
    return result;
}

function parser_jwt(token) {
    // 解析jwt
    let jwt_list = token.split('.')
    let payload = jwt_list[1]
    return JSON.parse(decodeURIComponent(escape(window.atob(payload.replace(/-/g, "+").replace(/_/g, "/")))))
}


function get_token_headers(is_refresh_token = false) {
    // 获取带token信息的http头部信息
    if (is_refresh_token === true) {
        return {'Authorization': 'Bearer ' + localStorage.getItem('refresh_token')}
    } else {
        return {'Authorization': 'Bearer ' + localStorage.getItem('token')}
    }

}

function refresh_token() {
    // 刷新token
    let token_headers = get_token_headers(true)
    axios.put(refresh_token_url, {headers: token_headers})
        .then(response => {
            if (response.data.status === 200) {
                localStorage.setItem('token', response.data.data.token)
            } else if (response.data.status === 401) {
                // refresh_token 已失效重定向到首页
            }
        })
        .catch(error => {
            console.log(error)
        })
}

function paramsToFormData(obj) {
    // js对象转FormData
    const formData = new FormData();
    Object.keys(obj).forEach((key) => {
        if (obj[key] instanceof Array) {
            obj[key].forEach((item) => {
                formData.append(key, item);
            });
            return;
        }
        formData.append(key, obj[key]);
    });
    return formData;
}


function user_logout() {
    // 用户退出登录
    localStorage.clear()
    window.location.href = './index.html'

}

async function upload_file(file) {
    // 文件上传
    let upload_form_data, upload_url;
    if (file instanceof Array) {
        // 批量上传
        upload_form_data = paramsToFormData({'files': file});
        upload_url = batch_upload_file_url
    } else {
        // 单文件上传
        upload_form_data = paramsToFormData({'file': file});
        upload_url = upload_file_url
    }
    let config = {
        'headers': get_token_headers(),
        'Content-Type': 'multipart/form-data'
    }
    return new Promise((resolve, reject) => {
        axios.post(upload_url, upload_form_data, config)
            .then(response => {
                if (response.status === 200 && response.data.code === 0) {
                    resolve(response.data.data);
                    return response.data.data;
                }
            })
            .catch(error => {
                reject(error.data)
                console.log(error)
            })
    });
}

function verify_user_token() {
    let token = localStorage.getItem('token')
    let user_info
    if (token != null) {
        user_info = parser_jwt(token)
        // 判断token有没有过期
        let now_timestamp = Date.parse(new Date()) / 1000
        console.log(now_timestamp)
        console.log(user_info.exp)
        if (user_info.exp < now_timestamp) {
            // token已过期
            layer.alert('登录状态已失效，请重新登录')
            window.location.href = '/house_rental/home_front/index.html'
        }
    } else {
        window.location.href = '/house_rental/home_front/index.html'
    }
    return user_info
}