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