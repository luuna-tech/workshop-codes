import { ZecoreItem } from './ZecoreItem';
import { WebClientItem } from './WebClientItem';

class ZecoreItemAdapter implements WebClientItem {
  protected zItem : ZecoreItem;

  constructor (zItem: ZecoreItem) {
    this.zItem = zItem;
  }

  get quantity() {
    return this.zItem.quantity;
  }

  get product()  {
    return {
      id: this.zItem.itemCode,
      name: this.zItem.itemName,
      baselineRate: this.zItem.baselineRate,
      finalRate: this.zItem.finalRate,
      image: {
       small: this.zItem.image
     }
    };
  }
}

export default ZecoreItemAdapter;
