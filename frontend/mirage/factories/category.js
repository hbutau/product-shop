import { Factory } from 'ember-cli-mirage';
import  faker from 'faker';


export default Factory.extend({
    // name(i) {return `Category ${i}`},
    name: faker.commerce.department
});
