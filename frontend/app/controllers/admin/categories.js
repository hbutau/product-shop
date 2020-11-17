import Controller from '@ember/controller';
import { action } from '@ember/object';

export default class AdminCategoriesController extends Controller {
    @action
    addNewCategory(id, name) {
        this.get('model').pushObject({id, name})
    }

    @action
    deleteCategory(category) {
        this.get('model').removeObject(category)
    }
}
