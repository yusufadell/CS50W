# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Language, HistoricalArticle, Article, RelatedArticle, Category, SubCategory, AssociateSubCategory, Tag, AssociateTag, Author, RelatedAuthor, ModificationType, HistoricalModification, Modification


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('id', 'language_code', 'language_name')


@admin.register(HistoricalArticle)
class HistoricalArticleAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'article_title',
        'article_text',
        'article_url',
        'time_created',
        'time_updated',
        'time_published',
        'default_language',
        'history_id',
        'history_date',
        'history_change_reason',
        'history_type',
        'history_user',
    )
    list_filter = (
        'time_created',
        'time_updated',
        'time_published',
        'default_language',
        'history_date',
        'history_user',
    )


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'article_title',
        'article_text',
        'article_url',
        'time_created',
        'time_updated',
        'time_published',
        'default_language',
    )
    list_filter = (
        'time_created',
        'time_updated',
        'time_published',
        'default_language',
    )


@admin.register(RelatedArticle)
class RelatedArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'article', 'related_article_id')
    list_filter = ('article',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')
    list_filter = ('category',)
    search_fields = ('name',)


@admin.register(AssociateSubCategory)
class AssociateSubCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'article', 'subcategory')
    list_filter = ('article', 'subcategory')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag_name')


@admin.register(AssociateTag)
class AssociateTagAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag', 'article')
    list_filter = ('tag', 'article')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'password',
        'last_login',
        'is_superuser',
        'username',
        'first_name',
        'last_name',
        'email',
        'is_staff',
        'is_active',
        'date_joined',
        'karma',
    )
    list_filter = (
        'last_login',
        'is_superuser',
        'is_staff',
        'is_active',
        'date_joined',
    )
    raw_id_fields = ('groups', 'user_permissions')


@admin.register(RelatedAuthor)
class RelatedAuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'article', 'author')
    list_filter = ('article', 'author')


@admin.register(ModificationType)
class ModificationTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'status')


@admin.register(HistoricalModification)
class HistoricalModificationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'time_modified',
        'article',
        'author',
        'modification_type',
        'history_id',
        'history_date',
        'history_change_reason',
        'history_type',
        'history_user',
    )
    list_filter = (
        'time_modified',
        'article',
        'author',
        'modification_type',
        'history_date',
        'history_user',
    )


@admin.register(Modification)
class ModificationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'article',
        'author',
        'modification_type',
        'time_modified',
    )
    list_filter = ('article', 'author', 'modification_type', 'time_modified')
