    /**
     * ts 2 date
     * @param ts 时间戳单位到秒
     * @returns {string}
     */
    function ts2date(ts) {
        var time = new Date(ts*1000);
        var y = time.getFullYear();
        var m = time.getMonth()+1;
        var d = time.getDate();
        var h = time.getHours();
        var mm = time.getMinutes();
        var s = time.getSeconds();
        return y+'-'+add0(m)+'-'+add0(d)+' '+add0(h)+':'+add0(mm)+':'+add0(s);
    }

    function add0(m){return m<10?'0'+m:m }

    /**
     * date 2 ts
     * @param date yyyy/mm/dd hh:mm:ss
     */
    function datestr2ts(y,m,d,h,min,s) {
        var date = y+'/' + m+'/'+d +' '+ h +':'+min +':'+s;
        //console.log('date '+date);
        //date = date.replace(/-/g,'/');
        var ts = new Date(date).getTime()/1000;
        //console.log('ts '+ts);
        return ts;
    }
    var emptyFile={"type":'',"name":'',"version":''};//,"content":''};
