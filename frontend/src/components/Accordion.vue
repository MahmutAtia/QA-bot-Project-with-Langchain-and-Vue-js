<script>
export default {
    name: 'Accordion',
    props: {
        title: {
            type: String,
            required: true
        },
        content: {
            type: String,
            required: true
        }
    },

    data() {
        return {
            isActive: false,
            contentHeight :'0px'
        }
    },
   
    methods: {
        toggleAccordion() {
            this.isActive = !this.isActive;
            setTimeout(() => {
            this.contentHeight = this.isActive ? 'auto' : '0px';
      }, 50);
        }
    }
   
    }


</script>



<template>
    <div class="accordion">
        <div class="accordion-item">
            <div class="accordion-title" @click="toggleAccordion" >
                <h2>{{ title }}</h2>
                <span class="icon" :class="{ rotate: isActive }">{{ isActive ? '-' : '+' }}</span>

            </div>

                <div class="accordion-content" v-show="isActive" >
                <p>{{ content }}</p>
            </div>
        </div>
    </div>

</template>

<style>

.accordion {
    width: 100%;
    max-width: 800px;
    margin: 20px auto;
}

.accordion-item {
    border-bottom: 1px solid #ddd;
}

.accordion-title {
    padding: 15px;
    font-weight: 600;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: space-between;
    background-color: #f9f9f9;
}

.icon {
    font-size: 30px;
    transition: transform 0.3s ease;
}

.icon.rotate {
    transform: rotate(180deg);
}


.accordion-content {
    padding: 15px;
    background-color: #f4f4f4;
    padding: 15px;
}



</style>