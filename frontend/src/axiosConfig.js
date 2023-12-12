import axios from "axios";


export const instance = axios.create({
    baseURL: "http://localhost:8000//invoke",
    headers: {
        "Content-Type": "application/json",
        accept: "application/json",
    },

});
