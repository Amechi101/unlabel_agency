# classroom_product

## DONE:

- make all foreign keys references instead of plain integers
- Add ProductReviewID reference

## TODO:

- Remove is_selected from the database, replace with a virtual attribute inside django.


## Nice to have:

- Rename to products
- Rename subject to product_category


# classroom_brand

## DONE:

- Make all foreign keys references instead of plain integers

## TODO:

# classroom_user

Users -> Creator | Brand

## TODO:

## Nice to Have:

- Rename is_creator -> is_creator (references user)
- Rename is_teacher -> is_brand

# classroom_productreview

## DONE:

- Create a 1-1 relationship between Product & ProductReview
- Make creator_id a foreign key

## TODO:

- Change type of review_image to array[String]

# classroom_productvariant

## TODO: Ignore

# classroom_product_variants_available

## TODO: Ignore

# classroom_creator

# TODO:

- Make instagram_handle unique

## Nice to have:

- Rename Creator to Creator

# classroom_user_groups

Django specific (ignore)

# classroom_user_user_permissions

Django specific (ignore)

