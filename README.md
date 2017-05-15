# django-nodelete-model

No Delete Model for django

## Requirements

* Django >= 1.4
* Python >= 2.7


## How to install

You can install django-nodelete-model using **pip**

    pip install django-nodelete-model

or via sources:

    python setup.py install


## Usage

Model:

```python
from django.db import models

from no_delete.models import NoDeleteModel


class Supplier(NoDeleteModel):
    name = models.CharField(max_length=255)
```

Manager:

```python
Supplier.objects.deleted_set()
Supplier.objects.all_with_deleted()
```

Hard Delete:

```python
supplier = Supplier.objects.get(id=1)
supplier.delete(hard=True)
```

Queryset:

```python
Supplier.objects.filter(id__in=[1, 2, 3]).delete(hard=True)
Supplier.objects.filter(id__in=[1, 2, 3]).delete() # keep supplier
Supplier.objects.filter(id__in=[1, 2, 3]).hard_delete()
```


Contributing
-------
1. Fork it
2. Create your feature branch (git checkout -b new-feature)
3. Commit your changes (git commit -am 'Add some feature')
4. Push to the branch (git push origin my-new-feature)
5. Create new Pull Request


Licence
-------------
The MIT License (MIT)

Copyright (c) 2017 Bahattin Çiniç

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE