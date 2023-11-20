### 0\. Inline styling

mandatory

Write an HTML page that displays a header and a footer.

Layout:

- Body:
    - no margin
    - no padding
- Header:
    - color #FF0000 (red)
    - height: 70px
    - width: 100%
- Footer:
    - color #00FF00 (green)
    - height: 60px
    - width: 100%
    - text `Best School` center vertically and horizontally
    - always at the bottom at the page

Requirements:

- You must use the `header` and `footer` tags
- You are not allowed to import any files
- You are not allowed to use the `style` tag in the `head` tag
- Use inline styling for all your tags

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2021/12/98f4ac1b0644512ce7ae91a9e8e61e8fe174911d.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231117T012515Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=57773b3be0a979f5ead2084057ec673607d2a127f589577f03145c5ec9fb7f89)

- File: `0-index.html`

### 1\. Head styling

mandatory

Write an HTML page that displays a header and a footer by using the `style` tag in the `head` tag (same as `0-index.html`)

Requirements:

- You must use the `header` and `footer` tags
- You are not allowed to import any files
- No inline styling
- You must use the `style` tag in the `head` tag

The layout must be exactly the same as `0-index.html`

- File: `1-index.html`

### 2\. CSS files

mandatory

Write an HTML page that displays a header and a footer by using CSS files (same as `1-index.html`)

Requirements:

- You must use the `header` and `footer` tags
- No inline styling
- You must have 3 CSS files:
    - `styles/2-common.css`: for global style (i.e. the `body` style)
    - `styles/2-header.css`: for header style
    - `styles/2-footer.css`: for footer style

The layout must be exactly the same as `1-index.html`

- File: `2-index.html, styles/2-common.css, styles/2-header.css, styles/2-footer.css`

### 3\. Zoning done!

mandatory

Write an HTML page that displays a header and footer by using CSS files (same as `2-index.html`)

Layout:

- Common:
    - no margin
    - no padding
    - font color: #484848
    - font size: 14px
    - font family: `Circular,"Helvetica Neue",Helvetica,Arial,sans-serif;`
    - [icon](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/icon.png "icon") in the browser tab
- Header:
    - color: white
    - height: 70px
    - width: 100%
    - border bottom 1px #CCCCCC
    - [logo](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/logo.png "logo") align on left and center vertically (20px space at the left)
- Footer:
    - color white
    - height: 60px
    - width: 100%
    - border top 1px #CCCCCC
    - text `Best School` center vertically and horizontally
    - always at the bottom at the page

Requirements:

- No inline style
- You are not allowed to use the `img` tag
- You are not allowed to use the `style` tag in the `head` tag
- All images must be stored in the `images` folder
- You must have 3 CSS files:
    - `styles/3-common.css`: for the global style (i.e `body` style)
    - `styles/3-header.css`: for the header style
    - `styles/3-footer.css`: for the footer style

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2021/12/2be1eda05a0d9097c210f2d3482a59aa858c5711.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231117T012515Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=58169322a546d12b90a44ab00734f8c5cde7853dab04a9727db56cf6882828ec)

- File: `3-index.html, styles/3-common.css, styles/3-header.css, styles/3-footer.css, images/`

### 4\. Search!

mandatory

Write an HTML page that displays a header, footer and a filters box with a search button.

Layout: (based on `3-index.html`)

- Container:
    - between `header` and `footer` tags, add a `div`:
        - classname: `container`
        - max width 1000px
        - margin top and bottom 30px - it should be 30px under the bottom of the `header` (screenshot)
        - center horizontally
- Filter section:
    - tag `section`
    - classname `filters`
    - inside the `.container`
    - color white
    - height: 70px
    - width: 100% of the container
    - border 1px #DDDDDD with radius 4px
- Button search:
    - tag `button`
    - text `Search`
    - font size: 18px
    - inside the section filters
    - background color #FF5A5F
    - text color #FFFFFF
    - height: 48px
    - width: 20% of the section filters
    - no borders
    - border radius: 4px
    - center vertically and at 30px of the right border
    - change opacity to 90% when the mouse is on the button

Requirements:

- You must use: `header`, `footer`, `section`, `button` tags
- No inline style
- You are not allowed to use the `img` tag
- You are not allowed to use the `style` tag in the `head` tag
- All images must be stored in the `images` folder
- You must have 4 CSS files:
    - `styles/4-common.css`: for the global style (`body` and `.container` styles)
    - `styles/3-header.css`: for the header style
    - `styles/3-footer.css`: for the footer style
    - `styles/4-filters.css`: for the filters style
- `4-index.html` **won’t be W3C valid**, don’t worry, it’s temporary

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2021/12/f959154b0cdf1cdf71ddef04e3787ef28462793e.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231117T012515Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=fb52ced3ff794be49313dffc428f3740e82ee24353ec15a193b3acc7826f2f02)

- File: `4-index.html, styles/4-common.css, styles/3-header.css, styles/3-footer.css, styles/4-filters.css, images/`

### 5\. More filters

mandatory

Write an HTML page that displays a header, footer and a filters box.

Layout: (based on `4-index.html`)

- Locations and Amenities filters:
    - tag: `div`
    - classname: `locations` for location tag and `amenities` for the other
    - inside the section filters (same level as the `button` Search)
    - height: 100% of the section filters
    - width: 25% of the section filters
    - border right #DDDDDD 1px only for the first left filter
    - contains a title:
        - tag: `h3`
        - font weight: 600  
            
        - text `States` or `Amenities`
    - contains a subtitle:
        - tag: `h4`
        - font weight: 400  
            
        - font size: 14px
        - text with fake contents

Requirements:

- You must use: `header`, `footer`, `section`, `button`, `h3`, `h4` tags
- No inline style
- You are not allowed to use the `img` tag
- You are not allowed to use the `style` tag in the `head` tag
- All images must be stored in the `images` folder
- You must have 4 CSS files:
    - `styles/4-common.css`: for the global style (`body` and `.container` styles)
    - `styles/3-header.css`: for the header style
    - `styles/3-footer.css`: for the footer style
    - `styles/5-filters.css`: for the filters style

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2021/12/85bfa50b96c2985723daa75b5e22f75ef16e2b2e.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231117T012515Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=d011995ab3682eb3b329ee6dcea86c66dd494e9c0194d8a0462ed71d081ed6df)

- File: `5-index.html, styles/4-common.css, styles/3-header.css, styles/3-footer.css, styles/5-filters.css, images/`

### 6\. It's (h)over

mandatory

Write an HTML page that displays a header, footer and a filters box with dropdown.

Layout: (based on `5-index.html`)

- Update Locations and Amenities filters to display a contextual dropdown when the mouse is on the filter `div`:
    - tag `ul`
    - classname `popover`
    - text should be fake now
    - inside each `div`
    - not displayed by default
    - color #FAFAFA
    - width same as the `div` filter
    - border #DDDDDD 1px with border radius 4px
    - no list display
    - Location filter has 2 levels of `ul`/`li`:
        - state -> cities
        - state name must be display in a `h2` tag (font size 16px)

Requirements:

- You must use: `header`, `footer`, `section`, `button`, `h3`, `h4`, `ul`, `li` tags
- No inline style
- You are not allowed to use the `img` tag
- You are not allowed to use the `style` tag in the `head` tag
- All images must be stored in the `images` folder
- You must have 4 CSS files:
    - `styles/4-common.css`: for the global style (`body` and `.container` styles)
    - `styles/3-header.css`: for the header style
    - `styles/3-footer.css`: for the footer style
    - `styles/6-filters.css`: for the filters style

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2021/12/6262f13624dca23ca19db505c44f88faddb82ebb.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231117T012515Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=1efd48139d799e1784c2654eb75206187275a61537efa8c2c95a1dc2dcd90edf) ![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2021/12/6e6bdfa13fa88a5f439d9e2b1dade826dd95529b.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231117T012515Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=ee763b975ea25925155df89b85b469043cb01bd8f32aca79919f38187a723fbc)

- File: `6-index.html, styles/4-common.css, styles/3-header.css, styles/3-footer.css, styles/6-filters.css, images/`

### 7\. Display results

mandatory

Write an HTML page that displays a header, footer, a filters box with dropdown and results.

Layout: (based on `6-index.html`)

- Add Places section:
    - tag: `section`
    - classname: `places`
    - same level as the filters section, inside `.container`
    - contains a title:
        - tag: `h1`
        - text: `Places`
        - align in the top left
        - font size: 30px
    - contains multiple “Places” as listing (horizontal or vertical) describe by:
        - tag: `article`
        - width: 390px
        - padding and margin 20px
        - border #FF5A5F 1px with radius 4px
        - contains the place name:
            - tag: `h2`
            - font size: 30px
            - center horizontally

Requirements:

- You must use: `header`, `footer`, `section`, `article`, `button`, `h1`, `h2`, `h3`, `h4`, `ul`, `li` tags
- No inline style
- You are not allowed to use the `img` tag
- You are not allowed to use the `style` tag in the `head` tag
- All images must be stored in the `images` folder
- You must have 5 CSS files:
    - `styles/4-common.css`: for the global style (i.e. `body` and `.container` styles)
    - `styles/3-header.css`: for the header style
    - `styles/3-footer.css`: for footer style
    - `styles/6-filters.css`: for the filters style
    - `styles/7-places.css`: for the places style

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2021/12/bca4d17fbe21a58b66a9d5d6b85df4801d147dd0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231117T012515Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=07d639f1382b9676aa17b41fea1bf55d9036109bca3887e8139ec94bc0970218)

- File: `7-index.html, styles/4-common.css, styles/3-header.css, styles/3-footer.css, styles/6-filters.css, styles/7-places.css, images/`

### 8\. More details

mandatory

Write an HTML page that displays a header, a footer, a filter box (dropdown list) and the result of the search.

Layout: (based on `7-index.html`)

Add more information to a Place `article`:

- Price by night:
    - tag: `div`
    - classname: `price_by_night`
    - same level as the place name
    - font color: #FF5A5F
    - border: #FF5A5F 4px rounded
    - min width: 60px
    - height: 60px
    - font size: 30px
    - align: the top right (with space)
- Information section:
    - tag: `div`
    - classname: `information`
    - height: 80px
    - border: top and bottom #DDDDDD 1px
    - contains (align vertically):
        - Number of guests:
            - tag: `div`
            - classname: `max_guest`
            - width: 100px
            - fake text
            - [icon](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/icon_group.png "icon")
        - Number of bedrooms:
            - tag: `div`
            - classname: `number_rooms`
            - width: 100px
            - fake text
            - [icon](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/icon_bed.png "icon")
        - Number of bathrooms:
            - tag: `div`
            - classname: `number_bathrooms`
            - width: 100px
            - fake text
            - [icon](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/icon_bath.png "icon")
- User section:
    - tag: `div`
    - classname: `user`
    - text `Owner: <fake text>`
    - `Owner` text should be in bold
- Description section:
    - tag: `div`
    - classname: `description`

Requirements:

- You must use: `header`, `footer`, `section`, `article`, `button`, `h1`, `h2`, `h3`, `h4`, `ul`, `li` tags
- No inline style
- You are not allowed to use the `img` tag
- You are not allowed to use the `style` tag in the `head` tag
- All images must be stored in the `images` folder
- You must have 5 CSS files:
    - `styles/4-common.css`: for the global style (i.e. `body` and `.container` styles)
    - `styles/3-header.css`: for the header style
    - `styles/3-footer.css`: for the footer style
    - `styles/6-filters.css`: for the filters style
    - `styles/8-places.css`: for the places style

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2021/12/f4b2d4ef94bd3a2e7e1ddefa81236595686d270e.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231117T012515Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=bc8a71a165fa10849016164bf12869784b9b6ae2874844ea92d9388c7de2d5ac)

- File: `8-index.html, styles/4-common.css, styles/3-header.css, styles/3-footer.css, styles/6-filters.css, styles/8-places.css, images/`

### 9\. Full details

#advanced

Write an HTML page that displays a header, footer, a filters box with dropdown and results.

Layout: (based on `8-index.html`)

Add more information to a Place `article`:

- List of Amenities:
    - tag `div`
    - classname `amenities`
    - margin top 40px
    - contains:
        - title:
            - tag `h2`
            - text `Amenities`
            - font size 16px
            - border bottom #DDDDDD 1px
        - list of amenities:
            - tag `ul` / `li`
            - no list style
            - icons on the left: [Pet friendly](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/icon_pets.png "Pet friendly"), [TV](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/icon_tv.png "TV"), [Wifi](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/icon_wifi.png "Wifi"), etc… feel free to add more
- List of Reviews:
    - tag `div`
    - classname `reviews`
    - margin top 40px
    - contains:
        - title:
            - tag `h2`
            - text `Reviews`
            - font size 16px
            - border bottom #DDDDDD 1px
        - list of review:
            - tag `ul` / `li`
            - no list style
            - a review is described by:
                - `h3` tag for the user/date description (font size 14px). Ex: “From Bob Dylan the 27th January 2017”
                - `p` tag for the text (font size 12px)

Requirements:

- You must use: `header`, `footer`, `section`, `article`, `button`, `h1`, `h2`, `h3`, `h4`, `ul`, `li` tags
- No inline style
- You are not allowed to use the `img` tag
- You are not allowed to use the `style` tag in the `head` tag
- All images must be stored in the `images` folder
- You must have 5 CSS files:
    - `styles/4-common.css`: for the global style (`body` and `.container` styles)
    - `styles/3-header.css`: for the header style
    - `styles/3-footer.css`: for the footer style
    - `styles/6-filters.css`: for the filters style
    - `styles/100-places.css`: for the places style

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2021/12/f54486a431a05ea3477e337e0e953686d3c6ffd0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231117T012515Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=4173a1f63f6b9a212b68e6c6573cde5b3967dbffd2630fd26606c595bf8a9c70)

- File: `100-index.html, styles/4-common.css, styles/3-header.css, styles/3-footer.css, styles/6-filters.css, styles/100-places.css, images/`

### 10\. Flex

#advanced

Improve the Places section by using [Flexible boxes](https://intranet.alxswe.com/rltoken/Xc-nBlQHexwNaCuKYpZ2-A "Flexible boxes") for all Place articles

[Flexbox Froggy](https://intranet.alxswe.com/rltoken/PZz46Gkdj5Mo9-AWERPhQA "Flexbox Froggy")

- File: `101-index.html, styles/4-common.css, styles/3-header.css, styles/3-footer.css, styles/6-filters.css, styles/101-places.css, images/`

### 11\. Responsive design

#advanced

Improve the page by adding [responsive design](https://intranet.alxswe.com/rltoken/9mRhZcLRxmsuCyF8q7S8Ww "responsive design") to display correctly in mobile or small screens.

Examples:

- no horizontal scrolling
- redesign search bar depending of the width
- etc.

- File: `102-index.html, styles/102-common.css, styles/102-header.css, styles/102-footer.css, styles/102-filters.css, styles/102-places.css, images/`

### 12\. Accessibility

#advanced

Improve the page by adding [Accessibility support](https://intranet.alxswe.com/rltoken/JO-zonPvzBUfqpYRZDAtug "Accessibility support")

Examples:

- Colors contrast
- Header tags
- etc.

---

Well done on completing this project! Let the world hear about this milestone achieved.

[Click here to tweet!](https://twitter.com/intent/tweet?text=I+have+successfully+completed+my+AirBnB+Web+Static+project+on+%23ALX_SE+%40facesofalxse)

---

- File: `103-index.html, styles/103-common.css, styles/103-header.css, styles/103-footer.css, styles/103-filters.css, styles/103-places.css, images/`
