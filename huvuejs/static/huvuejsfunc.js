$(document).ready(function () {

  new Vue({
    el: '#vuediv',
    data: {
      urls: {
        listImages: '/huvuejs/listImages/',
        addImages: '/huvuejs/addImages/',
        updImages: '/huvuejs/updImages/',
        delImages: '/huvuejs/delImages/',
        listYoutubeCodes: '/huvuejs/listYoutubeCodes/',
        addYoutubeCodes: '/huvuejs/addYoutubeCodes/',
        delYoutubeCodes: '/huvuejs/delYoutubeCodes/',
        showCategory: '/huvuejs/showCategory/',
        showColor: '/huvuejs/showColor/',
        imagesByCategory: '/huvuejs/imagesByCategory/',
        imagesByColor: '/huvuejs/imagesByColor/',
        
      },
      imgs: [],
      lastImg: '',
      codes: [],
      form: {
        code: '',
        id: '',
        image: '',
        cat:'',
        color: '',
      },
      categories: [],
      colors: [],
    },

    watch: {
      'message': function (novo, velho) {
        console.log(novo, velho)
        if (novo) {
          alert('Data changed!')
        }
      }
    },

    //start quando carregar pagina
    ready: function () {
      this.getImages();
      this.getYoutubeCodes();
      this.initCarrousel();
      this.initSelect();
      this.getCategories();
      this.getColors();
    },

    methods: {
      getImages: function () {
        const _vue = this
        this.$http.get(_vue.urls.listImages)
          .then(response => {
            //console.log(response.status);
            //console.log(response.data);
            _vue.imgs = response.data.result;
            // _vue.imgs = required('/media/' + response.data.result)
          });
      },
      addImages: function () {
        const _vue = this
        
        let input = document.getElementById('file');
        let data = new FormData();
        data.append('image', input.files[0]);
        console.log('##', input.files[0])
        
        this.$http.post(_vue.urls.addImages, data, { headers: { 'X-CSRFToken': getCookie('csrftoken')} })
          .then(response => {
            //_vue.form.image = '';
            _vue.lastImg = response.data.result.image;
          });          
      },
      updImages: function (id) {
        const _vue = this

        let input = document.getElementById('fil');
        let data = new FormData();
        data.append('image', input.files[0]);
        console.log('##', input.files)
        
        this.$http.post(_vue.urls.updImages+id+'/', data, { headers: { 'X-CSRFToken': getCookie('csrftoken')} })
          .then(response => {
            //_vue.form.image = '';
            //_vue.getImages()
            console.log(response)
          });          

      },
      delImages: function (id) {
        console.log(id)
        const _vue = this
        let token = getCookie('csrftoken');
        var url = _vue.urls.delImages+id
        this.$http.delete(url, { headers: { 'X-CSRFToken': token } })
          .then(response => {
            _vue.getImages()            
          });
      },

      getYoutubeCodes: function () {
        const _vue = this
        this.$http.get(_vue.urls.listYoutubeCodes)
          .then(response => {
            console.log(response.data);
            _vue.codes = response.data.result;
          });
        _vue.initCarrousel()  
      },
      addYoutubeCodes: function () {
        const _vue = this
        this.$http.post(_vue.urls.addYoutubeCodes,  _vue.form, { headers: { 'X-CSRFToken': getCookie('csrftoken') } })
          .then(response => {
            console.log(response.data);
            _vue.form.code = '';
          }).then(() => {
            _vue.getYoutubeCodes()
          });          
      },
      delYoutubeCodes: function (id) {
        const _vue = this
        let token = getCookie('csrftoken');
        var url = _vue.urls.delYoutubeCodes+id
        console.log(id)
        this.$http.delete(url, { headers: { 'X-CSRFToken': token } })
          .then(response => {
          }).then(() => {
            _vue.getYoutubeCodes()            
          });
      },

      getCategories: function () {
        const _vue = this
        this.$http.get(_vue.urls.showCategory)
          .then(response => {
            console.log(response.data);
            _vue.categories = response.data.result;
            // console.log(_vue.categories[1].fields.category)
          });
      },
      getColors: function () {
        const _vue = this
        this.$http.get(_vue.urls.showColor)
          .then(response => {
            _vue.colors = response.data.result;
          });
      },      
      imagesByCategory: function (){
        const _vue = this
        let fields = {
          params: {
            category: _vue.form.cat,
          }
        }
        // console.log('#', fields)
        this.$http.get(_vue.urls.imagesByCategory, fields)
          .then(response => {
            _vue.imgs = response.data.result;
          });          
      },

      imagesByColor: function (){
        const _vue = this
        let fields = {
          params: {
            color: _vue.form.color,
          }
        }
        this.$http.get(_vue.urls.imagesByColor, fields)
          .then(response => {
            _vue.imgs = response.data.result;
          });          
      },

      initCarrousel: function () {
        // Materialize
        setTimeout(() => {
          var elems = document.querySelectorAll('.carousel');
          M.Carousel.init(elems);

          window.movePrev = function () {
            var el = document.querySelector(".carousel");
            var l = M.Carousel.getInstance(el);
            l.prev(1);
          }
          window.moveNext = function () {
            var el = document.querySelector(".carousel");
            var l = M.Carousel.getInstance(el);
            l.next(1);
          }
        }, 300)
      },

      initSelect: function (){
        setTimeout(() => {
          var elems = document.querySelectorAll('select');
          M.FormSelect.init(elems);
        },300)                 
      }

    },

    computed: {
      
    }

  })

})
