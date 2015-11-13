//wx.config({
//    debug: true, // 开启调试模式,调用的所有api的返回值会在客户端alert出来，若要查看传入的参数，可以在pc端打开，参数信息会通过log打出，仅在pc端时才会打印。
//    appId: 'wx1d5a93e16a3a77e2', // 必填，公众号的唯一标识
//    timestamp: , // 必填，生成签名的时间戳
//    nonceStr: '', // 必填，生成签名的随机串
//    signature: '',// 必填，签名，见附录1
//    jsApiList: [] // 必填，需要使用的JS接口列表，所有JS接口列表见附录2
//});
wx.onMenuShareAppMessage({
    title: '张寻的简历', // 分享标题
    desc: '描述,这是最好的时代', // 分享描述
    link: 'http://www.dflbkj.cn/me/', // 分享链接
    imgUrl: 'http://www.dflbkj.cn/me/me/app/img/me.png', // 分享图标
    type: 'link', // 分享类型,music、video或link，不填默认为link
    dataUrl: '', // 如果type是music或video，则要提供数据链接，默认为空
    success: function () {
        // 用户确认分享后执行的回调函数
        alert("success");
    },
    cancel: function () {
        // 用户取消分享后执行的回调函数
        alert("cancel");
    }
})

wx.onMenuShareTimeline({
    title: '简历TO朋友圈', // 分享标题
    link: 'http://www.dflbkj.cn/me/', // 分享链接
    imgUrl: 'http://www.dflbkj.cn/me/me/app/img/computer.png', // 分享图标
    success: function () {
        // 用户确认分享后执行的回调函数
        alert("success");
    },
    cancel: function () {
        // 用户取消分享后执行的回调函数
        alert("cancel");
    }
});