# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import vk

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Post


@login_required
def ten_posts(request):
    social = request.user.social_auth.get(provider='vk-oauth2')
    access_token = social.extra_data.get('access_token')

    vk_session = vk.Session(access_token=access_token)
    vk_api = vk.API(vk_session, v='5.71')

    try:
        posts_response = vk_api.wall.get(count=10)
    except vk.api.VkAPIError as e:
        return render(request, 'ten_posts.html', context={'status': 'error', 'details': e.message})

    posts = posts_response['items']
    for post in posts:
        # save posts even if they already have been extracted earlier
        Post.objects.create(
            user=request.user,
            details=post,
            vk_id=post['id'],
            vk_owner_id=post['owner_id']
        )

    return render(
        request, 'ten_posts.html',
        context={'status': 'success', 'posts': posts}
    )
