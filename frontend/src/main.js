import './app.css';
import { mount } from 'svelte';
import Index from './routes/index.svelte';

console.log('Mounting the app...');

const app = mount(Index, { target: document.getElementById("app") });

export default app
