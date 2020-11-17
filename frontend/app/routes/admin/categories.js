import Route from '@ember/routing/route';

export default class AdminCategoriesRoute extends Route {
    model() {
        return this.store.findAll('category')
            }

    }
