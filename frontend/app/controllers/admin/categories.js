import Controller from '@ember/controller';
import { action } from '@ember/object';

export default class AdminCategoriesController extends Controller {
    @action
    addNewCategory(id, name) {
        this.store.createRecord('category', {id, name}).save();
    }

    @action
    deleteCategory(category) {
        category.destroyRecord();
    }
}
