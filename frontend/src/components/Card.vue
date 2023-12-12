
<script>
import {instance} from '../axiosConfig.js'
import Accordion from './Accordion.vue'

export default {
    name: 'Card',
    data() {
        return {
            query: '',
            result: '',
            loading : false,
            source_documents: [],
        };
    },
    methods: {
        async getAnswer() {
            this.loading = true;
            instance.post('', {
                input: {
                    query: this.query,

                },
                config: {},
                kwargs: {}
            }).then((response) => {
                console.log(response.data);
                this.result = response.data.output.result;
                this.source_documents = response.data.output.source_documents;
                this.loading = false
            }).catch((error) => {
                alert(error);
            });
        },
    },
    components: { Accordion }
}
   
</script>

<template>
    <div class="wrapper">
        <div class="card-title">
            <h2> Türk Anayasaya Istediginiz Soruyu Sorun !</h2>
        </div>
        
        <!-- Text input box -->
        <input class="query" type="text" v-model="query"  placeholder="Sorunuzu burade yazınız !"/>
        <button class="btn btn-primary" @click="getAnswer">Sorunuzu Gönder</button>


        <!-- Loading -->
        <div v-if="loading" class="loading">
            
            <h2>Loading...</h2>
        </div>

        <!-- Result -->
        <div v-if="result" class="result">
            <h2>Result</h2>
            <p>{{ result }}</p>
        </div>



        <!-- Source Documents -->
        <div v-if="source_documents.length > 0  && result != 'Bu sorunun cevabı bilmiyorum.'"  class="source-documents">
            <h2>Source Documents</h2>
            <Accordion v-for="(source_document, index) in source_documents" :key="index"
             :title="'Document ' + (index + 1)" :content="source_document.page_content" />
        </div>




    </div>

</template>

<style scoped>
/* .card {
  margin: 20px auto;
  margin-left: 100px;
  background-color: #f8f8f8;
  border-radius: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  padding: 20px;
  display: flex;
  flex-direction: column;
    justify-content: center;
  align-items: center;
  text-align: center;
  font-family: 'Poppins', sans-serif;
  color: #333;
  height: 700px; 
  width: 900px;

} */


.wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin: 20px auto;
  margin-left: 100px;
  background-color: #f8f8f8;
  border-radius: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  padding: 20px;
  font-family: 'Poppins', sans-serif;
  color: #333;
  width: 100%;
  margin: auto;
}
.query {
    width: 100%;
    padding: 12px;
    margin: 10px 0;
    border: 1px solid #ccc;
    border-radius: 6px;
    font-family: 'Poppins', sans-serif;
    color: #333;
    font-size: 16px;
}

.card-title {
    font-size: 1.8rem;
    font-weight: 600;
    margin-bottom: 20px;
}

.btn {
    padding: 12px 20px;
    border: none;
    border-radius: 6px;
    font-family: 'Poppins', sans-serif;
    color: #fff;
    font-size: 16px;
    font-weight: 500;
    background-color: #4caf50;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.btn:hover {
    background-color: #43a047;
}

.result,
.source-documents {
    margin-top: 30px;
    width: 100%;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    background-color: #fff;
    text-align: left;
    color: #333;
    font-family: 'Poppins', sans-serif;
    font-size: 16px;
    line-height: 1.6;
}
</style>
