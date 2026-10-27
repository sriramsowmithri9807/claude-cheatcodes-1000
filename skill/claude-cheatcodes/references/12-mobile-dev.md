# 12-mobile-dev

React Native, Flutter, Swift, Kotlin, Expo: push, offline sync, biometrics, camera, app store prep.

30 prompts. Search `## ` headings or ids; see index.md for the one-line list.

## Build a React Native App with Expo

**id:** `12-mobile-dev/expo-app` · **Difficulty:** intermediate · **Tags:** expo, react-native, mobile, typescript

**Placeholders:** [DESCRIBE YOUR APP], [YOUR FEATURES]

````text
Build a React Native app with Expo for: [DESCRIBE YOUR APP].

Stack: Expo SDK 51+ + TypeScript + NativeWind (Tailwind for RN)

Setup:
1. `npx create-expo-app --template` with TypeScript template
2. Folder structure: app/, components/, hooks/, utils/, constants/
3. Expo Router v3 (file-based routing)

Core features:
4. Navigation: Tab bar + Stack navigation
5. Safe area handling
6. Status bar control
7. Splash screen + app icon
8. Environment variables (EAS Secrets)

Shipping:
9. EAS Build: iOS (.ipa) + Android (.apk / .aab)
10. EAS Update: OTA updates for JS bundle
11. App Store / Play Store submission checklist

Output: complete app with [YOUR FEATURES] implemented.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Create Expo Config Plugins

**id:** `12-mobile-dev/expo-config-plugins` · **Difficulty:** advanced · **Tags:** expo, config-plugins, native, advanced

**Placeholders:** [DESCRIBE: permission, entitlement, plist entry, Gradle config, native module]

````text
Create an Expo config plugin to add native functionality to my managed Expo app.

Native functionality needed: [DESCRIBE: permission, entitlement, plist entry, Gradle config, native module]

What config plugins are:
- Modify native iOS/Android project WITHOUT ejecting
- Applied during `expo prebuild` (or EAS Build)
- Written in JavaScript/TypeScript

Plugin anatomy:
1. `withAndroidManifest`: add permissions, activities
2. `withInfoPlist`: add iOS permission descriptions
3. `withEntitlements`: add iOS capabilities
4. `withGradleProperties`: modify gradle.properties
5. `withPodfile`: modify Podfile
6. `withXcodeProject`: advanced Xcode modifications

Implement for my use case:
7. Write the plugin function
8. Register in app.json: `"plugins": ["./my-plugin"]`
9. Test: `expo prebuild --clean`
10. Publish: share as npm package

Output: complete config plugin for my native requirement.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Build and Deploy with EAS

**id:** `12-mobile-dev/expo-eas` · **Difficulty:** intermediate · **Tags:** expo, eas, deployment, mobile

**Placeholders:** [DESCRIBE]

````text
Build and deploy my Expo app with EAS (Expo Application Services).

App: [DESCRIBE]

**EAS Build**:
1. `eas build:configure` — create eas.json
2. Build profiles: development, preview, production
3. iOS: Apple Developer account setup, certificates, profiles
4. Android: keystore management
5. Build command: `eas build --platform all --profile production`
6. Build cache: speed up builds

**EAS Update (OTA)**:
7. Update JS bundle without App Store review
8. Channels: production, staging, preview
9. Rollback bad update
10. `eas update --channel production --message "Fix login bug"`

**EAS Submit**:
11. `eas submit --platform ios` → App Store Connect
12. `eas submit --platform android` → Play Store

**GitHub Actions**: automate build + submit on push to main.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Get Started with Flutter

**id:** `12-mobile-dev/flutter-basics` · **Difficulty:** intermediate · **Tags:** flutter, dart, mobile, cross-platform

**Placeholders:** [DESCRIBE YOUR APP], [YOUR CORE FEATURE]

````text
Build a Flutter app for: [DESCRIBE YOUR APP].

Stack: Flutter 3.x + Dart

1. **Project setup**: `flutter create myapp --org com.example`
2. **Folder structure**: lib/features/, lib/core/, lib/shared/
3. **State management**: Riverpod 2.0 (recommended for new projects)
4. **Navigation**: GoRouter (declarative, deep link support)
5. **HTTP client**: Dio with interceptors for auth
6. **Local storage**: Hive (NoSQL) or Drift (SQLite with ORM)
7. **Theme**: Material 3 with custom color scheme
8. **Responsive**: work on mobile + tablet + desktop
9. **Testing**: widget tests + integration tests
10. **Build**: `flutter build apk` (Android) + `flutter build ipa` (iOS)

Implement: [YOUR CORE FEATURE] end-to-end.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Make React Native App Accessible

**id:** `12-mobile-dev/react-native-accessibility` · **Difficulty:** intermediate · **Tags:** react-native, accessibility, a11y, mobile

````text
Make my React Native app fully accessible.

Compliance target: WCAG 2.1 AA + Apple HIG + Google Material accessibility

1. **VoiceOver / TalkBack**: test with screen reader
2. **accessibilityLabel**: descriptive labels for all interactive elements
3. **accessibilityRole**: button, link, header, tab, etc.
4. **accessibilityState**: checked, disabled, selected, expanded
5. **accessibilityHint**: additional context for complex actions
6. **Focus management**: after modal opens, focus moves inside
7. **Dynamic type**: support iOS dynamic font sizes
8. **Color contrast**: meet 4.5:1 ratio for all text
9. **Touch targets**: minimum 44x44pt
10. **Motion**: respect `prefers-reduced-motion`
11. **Accessible images**: `accessible + accessibilityLabel` or `accessibilityElementsHidden` for decorative
12. **Forms**: label each input field

Test with: Accessibility Inspector (iOS), TalkBack (Android).
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Build Smooth Animations in React Native

**id:** `12-mobile-dev/react-native-animations` · **Difficulty:** advanced · **Tags:** react-native, animations, reanimated, mobile

**Placeholders:** [DESCRIBE: screen transitions, gesture interactions, loading states, etc.]

````text
Build smooth animations for my React Native app.

Animations needed: [DESCRIBE: screen transitions, gesture interactions, loading states, etc.]

Using: React Native Reanimated 3 + Gesture Handler

1. **Shared values**: `useSharedValue` — the foundation
2. **Animated style**: `useAnimatedStyle` — apply to components
3. **Spring animation**: natural bouncy physics
4. **Timing animation**: CSS-like with easing
5. **Gesture-driven**: swipe cards, drag elements
6. **Enter/exit animations**: `Entering` and `Exiting` presets
7. **Layout animations**: `Layout` prop for automatic transitions
8. **Interpolation**: map value ranges (scroll → opacity)
9. **Gesture + animation**: pinch to zoom, swipe to dismiss
10. **Performance**: everything runs on UI thread (60/120fps)

Output: animated components for each of my use cases.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Connect React Native to Backend API

**id:** `12-mobile-dev/react-native-api` · **Difficulty:** intermediate · **Tags:** react-native, api, tanstack-query, axios

**Placeholders:** [DESCRIBE YOUR BACKEND API]

````text
Connect my React Native app to a backend API.

API: [DESCRIBE YOUR BACKEND API]
Auth: [JWT / OAuth]

1. **HTTP client**: Axios with base URL + interceptors
2. **Auth interceptor**: attach token to every request
3. **Refresh interceptor**: auto-refresh expired token
4. **Error interceptor**: handle 401 (logout), 5xx (show error)
5. **TanStack Query**: data fetching, caching, background refetch
6. **Optimistic updates**: update UI before server confirms
7. **Infinite queries**: paginated lists with infinite scroll
8. **Mutations**: POST/PUT/DELETE with loading/error states
9. **Offline**: cache results, show stale data when offline
10. **Retry**: automatic retry on network failure
11. **Environment**: .env for API URL per environment
12. **TypeScript**: typed API responses with Zod validation

Output: API client + TanStack Query hooks for my endpoints.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Implement Authentication in React Native

**id:** `12-mobile-dev/react-native-auth` · **Difficulty:** intermediate · **Tags:** react-native, auth, expo, security

````text
Implement authentication in my React Native app.

Auth methods: [EMAIL+PASSWORD / SOCIAL LOGIN / BIOMETRIC]
Backend: [DESCRIBE OR Firebase/Supabase]

1. **Token storage**: expo-secure-store for access + refresh tokens
2. **Auto-login**: check stored token on app start
3. **Token refresh**: transparently refresh expired tokens
4. **Logout**: clear all stored data
5. **Social login**:
   - Google: `@react-native-google-signin/google-signin`
   - Apple: `expo-apple-authentication` (required on iOS)
6. **Biometric**: Face ID / Fingerprint (expo-local-authentication)
7. **Deep link callback**: OAuth redirect back to app
8. **Logged-in check**: protected routes in Expo Router
9. **Session persistence**: stay logged in after app restart
10. **Multi-account**: switch between accounts

Output: auth context + login screen + protected navigation.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Run Background Tasks in React Native

**id:** `12-mobile-dev/react-native-background-tasks` · **Difficulty:** advanced · **Tags:** react-native, background, tasks, mobile

**Placeholders:** [DESCRIBE: location tracking, data sync, download, notifications]

````text
Run background tasks in my React Native app.

Background needs: [DESCRIBE: location tracking, data sync, download, notifications]

**iOS background modes** (must declare in Info.plist):
1. Background fetch: periodically wake app to sync data
2. Remote notifications: wake on push to process
3. Background processing: long tasks when device charging
4. Location updates: always-on GPS tracking

**Android**:
5. WorkManager: deferrable background work (sync, upload)
6. Foreground Service: with persistent notification (location, audio)
7. JobScheduler: periodic tasks

**Expo libraries**:
8. `expo-background-fetch`: cross-platform periodic sync
9. `expo-task-manager`: define and manage background tasks
10. `expo-location`: background location tracking

Limitations: iOS aggressively limits background — understand the constraints.
Battery optimization: efficient background work.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Implement Biometric Authentication

**id:** `12-mobile-dev/react-native-biometrics` · **Difficulty:** intermediate · **Tags:** react-native, biometrics, security, expo

````text
Add biometric authentication (Face ID, Touch ID, Fingerprint) to my React Native app.

Using: `expo-local-authentication`

1. **Check availability**: is biometric available and enrolled?
2. **Types**: face recognition, fingerprint, iris
3. **Authentication**: prompt with reason, get result
4. **Fallback**: if biometric fails → fall back to PIN/password
5. **Store credentials**: biometric gates access to stored credentials (expo-secure-store)
6. **First time**: user enables biometric in settings screen
7. **Persist choice**: remember user's biometric preference
8. **Re-auth**: require biometric on app resume (sensitive apps)
9. **Android**: handle API differences between Android versions
10. **Accessibility**: graceful degradation if no biometric hardware

Flow: app launch → check biometric preference → authenticate → show app.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Add Camera and Media Features

**id:** `12-mobile-dev/react-native-camera` · **Difficulty:** intermediate · **Tags:** react-native, camera, expo, media

**Placeholders:** [DESCRIBE: photo capture, video, QR scan, face detection]

````text
Add camera and media features to my React Native app.

Features needed: [DESCRIBE: photo capture, video, QR scan, face detection]

Using: expo-camera + expo-image-picker + expo-media-library

1. **Camera permissions**: request with usage description
2. **Photo capture**: take photo, display preview, save
3. **Video recording**: start/stop recording
4. **Gallery picker**: select existing photos/videos
5. **Image manipulation**: resize, crop, compress (expo-image-manipulator)
6. **Upload**: multipart upload to backend or S3 presigned URL
7. **QR code scanner**: expo-barcode-scanner
8. **Face detection**: camera + face bounding box
9. **File storage**: save to device gallery (expo-media-library)
10. **Permission flow**: graceful handling when denied

Output: camera screen component + upload integration.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Build a Real-Time Chat in React Native

**id:** `12-mobile-dev/react-native-chat` · **Difficulty:** advanced · **Tags:** react-native, chat, websockets, mobile

````text
Build real-time chat in my React Native app.

Using: Socket.io + React Native GiftedChat

1. **Socket connection**: connect on login, disconnect on logout
2. **Authentication**: send token on WebSocket handshake
3. **GiftedChat setup**: renderItem, renderBubble, renderInput
4. **Message types**: text, image, voice, emoji
5. **Delivery receipts**: sent → delivered → read
6. **Typing indicator**: show when other user is typing
7. **Pagination**: load older messages on scroll up
8. **Push notifications**: receive messages when app is background
9. **Image messages**: pick from gallery, upload, display
10. **Voice messages**: record, visualize waveform, play
11. **Online presence**: show online/offline status
12. **Message actions**: long press → reply, copy, delete

Output: complete chat screen component.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Implement Deep Links in React Native

**id:** `12-mobile-dev/react-native-deep-links` · **Difficulty:** intermediate · **Tags:** react-native, deep-links, expo-router, mobile

````text
Implement deep links in my React Native app.

Links to handle:
- `myapp://post/123` — open specific post
- `https://myapp.com/post/123` — universal link (opens app if installed)

**With Expo Router**:
1. Configure URL scheme in `app.json`
2. Configure associated domain for universal links
3. File-based routes handle deep links automatically
4. Dynamic routes: `app/post/[id].tsx`
5. Test: `npx uri-scheme open myapp://post/123 --ios`

**Universal links setup**:
6. iOS: `apple-app-site-association` file on your domain
7. Android: `assetlinks.json` file on your domain

**Navigation on deep link**:
8. App closed: open to correct screen
9. App open: navigate without closing current session
10. Auth guard: redirect to login if not authenticated, then to deep link destination after

Output: complete deep link configuration.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Build Forms in React Native

**id:** `12-mobile-dev/react-native-forms` · **Difficulty:** intermediate · **Tags:** react-native, forms, validation, mobile

**Placeholders:** [DESCRIBE YOUR FORMS]

````text
Build beautiful, validated forms in React Native.

Forms needed: [DESCRIBE YOUR FORMS]

Using: react-hook-form + Zod

1. **Text inputs**: text, email, password, number, phone
2. **Keyboard types**: numeric, email-address, phone-pad
3. **Auto-advance**: next field on return key
4. **Validation**: real-time with Zod schema
5. **Error display**: under each field, shake animation
6. **Date picker**: native date picker or custom
7. **Dropdown select**: modal picker for select fields
8. **Image upload**: tap to select photo from gallery/camera
9. **Multi-step form**: wizard with progress indicator
10. **Keyboard avoidance**: scroll up when keyboard covers input
11. **Submit loading**: disable button, show spinner during submit
12. **Server errors**: map server validation to form fields

Output: complete form components.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Add Maps to React Native App

**id:** `12-mobile-dev/react-native-maps` · **Difficulty:** intermediate · **Tags:** react-native, maps, mapbox, location

**Placeholders:** [DESCRIBE: show user location, display markers, route, geofencing]

````text
Add maps and location features to my React Native app.

Features: [DESCRIBE: show user location, display markers, route, geofencing]

Using: react-native-maps (Google Maps / Apple Maps) or Mapbox

1. **Location permission**: request in foreground and background
2. **User location**: show blue dot, center on user
3. **Map markers**: custom markers with callouts
4. **Polylines**: draw route on map
5. **Clustering**: cluster nearby markers at low zoom
6. **Offline maps**: cache map tiles
7. **Geofencing**: alert when user enters/exits area
8. **Address search**: autocomplete address input
9. **Reverse geocode**: coords → human readable address
10. **Directions**: turn-by-turn (integrate with Google Maps / Apple Maps app)

Performance: limit re-renders when location updates frequently.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Handle Audio and Video in React Native

**id:** `12-mobile-dev/react-native-media` · **Difficulty:** intermediate · **Tags:** react-native, audio, video, expo

**Placeholders:** [DESCRIBE: music player, video streaming, voice recording, podcast player]

````text
Add audio and video capabilities to my React Native app.

Features: [DESCRIBE: music player, video streaming, voice recording, podcast player]

Using: expo-av (or expo-audio + expo-video for newer Expo)

**Audio**:
1. Playback: load, play, pause, seek, speed control
2. Background audio: play while app is backgrounded
3. Lock screen controls: media controls on lock screen
4. Recording: record audio, save to file
5. Streaming: play audio from URL

**Video**:
6. Fullscreen player
7. Custom controls overlay
8. Picture-in-picture (iOS)
9. Video thumbnail generation

**Optimizations**:
10. Buffer management for smooth streaming
11. Quality switching for adaptive bitrate
12. Offline download for later playback

Output: MediaPlayer component with all controls.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Add In-App Purchases to React Native

**id:** `12-mobile-dev/react-native-monetization` · **Difficulty:** advanced · **Tags:** react-native, iap, monetization, expo

````text
Add in-app purchases to my React Native app.

Using: `react-native-iap` or Expo In-App Purchases

Product types:
1. **Consumable**: one-time purchase (coin pack)
2. **Non-consumable**: permanent unlock (remove ads)
3. **Auto-renewable subscription**: monthly/annual plan

Implementation:
4. Set up products in App Store Connect + Google Play Console
5. Initialize IAP connection
6. Fetch available products
7. Purchase flow: purchase → validate receipt → unlock
8. **Receipt validation** (critical): validate on YOUR backend, not client
9. **Subscription status**: check on app launch
10. **Restore purchases**: restore button for non-consumables
11. **Error handling**: purchase cancelled, payment declined
12. **RevenueCat SDK**: simplifies all of the above (recommended)

Output: complete IAP integration with RevenueCat.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Master React Native Navigation

**id:** `12-mobile-dev/react-native-navigation` · **Difficulty:** intermediate · **Tags:** react-native, navigation, expo-router, mobile

**Placeholders:** [DESCRIBE YOUR SCREENS AND NAVIGATION FLOW]

````text
Implement navigation in my React Native app.

App structure: [DESCRIBE YOUR SCREENS AND NAVIGATION FLOW]

Using: Expo Router v3 (file-based, like Next.js for mobile)

1. **File-based routing**: app/(tabs)/, app/(auth)/, app/[id].tsx
2. **Tab navigation**: bottom tab bar with icons and badges
3. **Stack navigation**: push/pop with header customization
4. **Modal screens**: bottom sheet style modals
5. **Deep links**: handle URL scheme (myapp://post/123)
6. **Auth gates**: redirect to login if not authenticated
7. **Type-safe navigation**: typed route params
8. **Transitions**: custom animations between screens
9. **Drawer navigation**: side menu for settings
10. **Dynamic routes**: `app/posts/[id].tsx`

Output: complete navigation setup for my app structure.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Implement Push Notifications

**id:** `12-mobile-dev/react-native-notifications` · **Difficulty:** intermediate · **Tags:** react-native, notifications, expo, mobile

**Placeholders:** [DESCRIBE: marketing, transactional, real-time events]

````text
Implement push notifications in my React Native + Expo app.

Notification types: [DESCRIBE: marketing, transactional, real-time events]

1. **Setup**: expo-notifications + EAS configuration
2. **Permission request**: ask for permission with context
3. **Device token**: get Expo push token, send to your backend
4. **Local notifications**: schedule without server
5. **Remote notifications**: send from backend via Expo Push API
6. **Rich notifications**: title, body, image, actions
7. **Notification handling**:
   - App in foreground: show in-app toast
   - App in background: system notification
   - App closed: open to specific screen on tap
8. **Deep linking**: notification tap → specific screen
9. **Badge count**: update app icon badge
10. **Category actions**: quick reply, dismiss buttons

Backend: endpoint to store tokens + send notifications.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Build Offline-First React Native App

**id:** `12-mobile-dev/react-native-offline` · **Difficulty:** advanced · **Tags:** react-native, offline, sync, mobile

**Placeholders:** [DESCRIBE]

````text
Build offline-first functionality for my React Native app.

Data that needs to work offline: [DESCRIBE]

1. **Local database**: SQLite via expo-sqlite + DrizzleORM
2. **Data sync**: sync when connection is restored
3. **Conflict resolution**: last-write-wins or user choice
4. **Optimistic updates**: show result immediately, sync in background
5. **Network detection**: `@react-native-community/netinfo`
6. **Offline UI**: show offline banner, disable online-only features
7. **Background sync**: sync when app comes to foreground
8. **Retry queue**: queue failed requests, retry on reconnect
9. **Partial sync**: only sync changed records (delta sync)
10. **File sync**: cache media files for offline viewing

Pattern: TanStack Query with persistQueryClient for offline caching.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Integrate Payments in React Native

**id:** `12-mobile-dev/react-native-payments` · **Difficulty:** intermediate · **Tags:** react-native, stripe, payments, mobile

````text
Integrate payment processing in my React Native app.

Using: Stripe React Native SDK

1. **Installation**: `@stripe/stripe-react-native`
2. **Setup**: StripeProvider with publishable key
3. **Payment Sheet**: prebuilt UI (easiest, most conversions)
   - Create PaymentIntent on backend
   - Initialize and present payment sheet
   - Confirm result
4. **Card field**: manual card entry form
5. **Apple Pay**: `ApplePayButton`, Works in iOS only
6. **Google Pay**: `GooglePayButton`, Android only
7. **Link (Stripe Link)**: save payment methods across merchants
8. **Subscriptions**: create subscription via backend + Stripe
9. **3D Secure**: automatically handled by Payment Sheet
10. **Receipts**: send email receipt from backend webhook
11. **Testing**: Stripe test cards (4242 4242...)

Output: complete payment integration with backend.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Optimize React Native Performance

**id:** `12-mobile-dev/react-native-performance` · **Difficulty:** advanced · **Tags:** react-native, performance, optimization, mobile

**Placeholders:** [DESCRIBE: slow list, janky animations, slow startup, large bundle]

````text
Optimize my React Native app's performance.

Current issues: [DESCRIBE: slow list, janky animations, slow startup, large bundle]

1. **FlatList optimization**:
   - `getItemLayout` for uniform item heights
   - `keyExtractor` stability
   - `windowSize` tuning
   - `maxToRenderPerBatch`
2. **Memo**: `React.memo`, `useMemo`, `useCallback`
3. **Hermes engine**: enable Hermes for faster JS startup
4. **New Architecture**: enable React Native's new architecture (JSI)
5. **Image optimization**: FastImage, resize before upload, placeholder
6. **Bundle size**: analyze with `react-native-bundle-visualizer`
7. **Animation**: only use Reanimated (runs on UI thread)
8. **FlashList**: replace FlatList for large lists
9. **Startup time**: defer non-critical initialization
10. **Memory**: avoid memory leaks in navigation and event listeners

Profile first with Flipper or Xcode Instruments.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Secure a React Native App

**id:** `12-mobile-dev/react-native-security` · **Difficulty:** advanced · **Tags:** react-native, security, mobile, encryption

````text
Implement security best practices for my React Native app.

1. **Certificate pinning**: reject MITM attacks on API calls
   - `react-native-ssl-pinning`
   - Pin certificate SHA256 hash
2. **Secure storage**: never store secrets in AsyncStorage
   - expo-secure-store for sensitive data
   - MMKV with encryption for app data
3. **Root/jailbreak detection**: `react-native-device-info`
4. **Screenshot prevention**: block screenshots on sensitive screens
5. **Obfuscation**: obfuscate JS bundle (ProGuard + Metro config)
6. **Environment variables**: never hardcode API keys
   - EAS Secrets for build-time secrets
   - Backend serves keys, not hardcoded in app
7. **Code protection**: enable Hermes, minimize source maps
8. **Biometric auth**: gate sensitive operations
9. **Session timeout**: logout after inactivity
10. **Clipboard**: clear clipboard after copy of sensitive data
11. **Deep link validation**: validate origin of deep links
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## State Management in React Native

**id:** `12-mobile-dev/react-native-state` · **Difficulty:** intermediate · **Tags:** react-native, zustand, state, mobile

**Placeholders:** [DESCRIBE: auth, cart, settings, real-time data, etc.], [DESCRIBE]

````text
Set up state management for my React Native app.

App type: [DESCRIBE]
State needs: [DESCRIBE: auth, cart, settings, real-time data, etc.]

**Options**:
1. **React Context**: for simple global state (theme, auth)
2. **Zustand**: most popular, simple, performant
3. **Jotai**: atomic state model
4. **Redux Toolkit**: for complex apps with devtools

**For MY app** (using Zustand):
5. Store setup for each domain (auth store, cart store)
6. Persist to MMKV for offline/restart persistence
7. Async actions in store
8. Selectors to prevent re-renders
9. DevTools: react-native-debugger integration
10. React Query for server state (keep server/client state separate)

Output: complete Zustand stores for my app + TanStack Query setup.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Manage Storage in React Native

**id:** `12-mobile-dev/react-native-storage` · **Difficulty:** intermediate · **Tags:** react-native, storage, async-storage, sqlite

**Placeholders:** [DESCRIBE: user preferences, offline data, cache, etc.]

````text
Implement data persistence in my React Native app.

Data to persist: [DESCRIBE: user preferences, offline data, cache, etc.]

Storage options:
1. **AsyncStorage**: key-value for simple preferences
   - When to use: settings, auth tokens, simple state
   - Limitation: strings only, 6MB limit

2. **MMKV** (recommended over AsyncStorage):
   - 10x faster than AsyncStorage
   - Synchronous API
   - Use via react-native-mmkv

3. **SQLite** (expo-sqlite):
   - Full relational database
   - For complex offline-first data
   - DrizzleORM for SQLite in React Native

4. **Secure Storage** (expo-secure-store):
   - Keychain (iOS) / Keystore (Android)
   - For sensitive data: auth tokens, encryption keys

For my use case: which to use and implementation.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Test React Native Apps

**id:** `12-mobile-dev/react-native-testing` · **Difficulty:** intermediate · **Tags:** react-native, testing, jest, detox

**Placeholders:** [DESCRIBE]

````text
Write tests for my React Native app.

App: [DESCRIBE]

**Unit + Component tests** (Jest + RNTL):
1. Setup: jest-expo preset
2. Component rendering tests
3. User interaction: `fireEvent.press`, `fireEvent.changeText`
4. Navigation testing: mock navigation
5. Async tests: API calls, loading states

**E2E tests** (Detox):
6. Detox setup for iOS + Android
7. First test: launch → navigate → interact → assert
8. Text matchers: `by.id()`, `by.text()`, `by.type()`
9. Actions: tap, longPress, typeText, scroll
10. Assertions: `expect(el).toBeVisible()`, `toHaveText()`
11. Network mocking in E2E
12. CI: run E2E on iOS simulator in GitHub Actions

Output: unit test suite + Detox E2E for critical flows.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Build UI Component Library for React Native

**id:** `12-mobile-dev/react-native-ui` · **Difficulty:** intermediate · **Tags:** react-native, ui, components, design-system

**Placeholders:** [DESCRIBE YOUR DESIGN: minimal, colorful, corporate, etc.]

````text
Build a UI component library for my React Native app.

Design language: [DESCRIBE YOUR DESIGN: minimal, colorful, corporate, etc.]

Components to build:
1. **Button**: primary, secondary, ghost, destructive; sizes: sm/md/lg; loading state
2. **Input**: text, password, search with icon, error state
3. **Card**: with shadow, border, press state
4. **Avatar**: image with fallback initials, size variants
5. **Badge**: notification count, status dot
6. **Modal**: bottom sheet + center modal
7. **Toast**: auto-dismiss notifications
8. **ProgressBar + Spinner**
9. **ListItem**: icon + title + subtitle + right element
10. **EmptyState**: illustration + title + CTA

Design tokens: colors, spacing, typography, shadows.
Dark mode support.
Accessibility: testID, accessibilityLabel, role.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Build App Widgets for iOS and Android

**id:** `12-mobile-dev/react-native-widget` · **Difficulty:** advanced · **Tags:** react-native, widgets, ios, android

````text
Build home screen widgets for my React Native app.

**iOS Widget** (SwiftUI, in Expo managed workflow via config plugin):
1. Create native iOS widget extension
2. Widget sizes: small, medium, large
3. Timeline provider: update widget data on schedule
4. App group: share data between app and widget
5. Widget configuration: user customizable
6. Deep link from widget tap to specific screen

**Android Widget** (Kotlin/Glance, similarly via config plugin):
7. AppWidgetProvider
8. RemoteViews or Jetpack Glance (Compose-based)
9. Update on alarm/broadcast

**Data sharing**:
10. App Group (iOS) / Content Provider (Android) to share data
11. React Native → widget: update when app changes data

Note: widgets require native code → use Expo Dev Client (not Go).
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Configure native module integrations in [PLATFORM] for [NATIVE_FEATURE]

**id:** `12-mobile-dev/configure-native-module-integrations-in-platform-for-native-feature` · **Difficulty:** beginner/intermediate/advanced · **Tags:** mobile, expo, react-native, app, flutter, background, biometric, camera, sqlite, kotlin, react, swift, keychain

**Variant group** (9 generated prompts collapsed). Pick one value per placeholder:
- `[PLATFORM]`: Expo Go | Flutter | Kotlin (Android) | React Native | Swift (iOS)
- `[NATIVE_FEATURE]`: Keychain credential storage | SQLite database local syncing | background coordinates tracking | biometric login workflows | camera capture handlers
- `[APP_TYPE]`: fitness metric dashboards | offline-first text notes apps | photo uploads feeds | ride-sharing maps displays

````text
Configure [NATIVE_FEATURE] using native bindings in [PLATFORM] for [APP_TYPE]. Keep code optimized for performance and battery consumption.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Claude Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` and modify requirements based on your development environment and stack
- Use `--extended-thinking` mode for in-depth optimization suggestions

**Covers:** configure-native-module-integrations-in-expo-go-for-background-coordinates-tracking, configure-native-module-integrations-in-expo-go-for-biometric-login-workflows, configure-native-module-integrations-in-flutter-for-camera-capture-handlers, configure-native-module-integrations-in-kotlin-android-for-sqlite-database-local-syncing, configure-native-module-integrations-in-react-native-for-background-coordinates-tracking, configure-native-module-integrations-in-react-native-for-camera-capture-handlers, configure-native-module-integrations-in-swift-ios-for-biometric-login-workflows, configure-native-module-integrations-in-swift-ios-for-keychain-credential-storage, configure-native-module-integrations-in-swift-ios-for-sqlite-database-local-syncing


## Implement [NATIVE_FEATURE] in [PLATFORM]

**id:** `12-mobile-dev/implement-native-feature-in-platform` · **Difficulty:** beginner/intermediate/advanced · **Tags:** mobile, biometric, expo, react-native, app, flutter, react, kotlin, camera, keychain, push, sqlite

**Variant group** (13 generated prompts collapsed). Pick one value per placeholder:
- `[PLATFORM]`: Expo Go | Flutter | Kotlin (Android) | React Native
- `[NATIVE_FEATURE]`: Keychain credential storage | SQLite database local syncing | biometric login workflows | camera capture handlers | push notifications hooks
- `[APP_TYPE]`: fitness metric dashboards | mobile e-commerce shopping carts | offline-first text notes apps | photo uploads feeds | ride-sharing maps displays

````text
Build and implement [NATIVE_FEATURE] in [PLATFORM] for [APP_TYPE]. Include full code, permissions handling, and error fallback layouts.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Claude Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` and modify requirements based on your development environment and stack
- Use `--extended-thinking` mode for in-depth optimization suggestions

**Covers:** implement-biometric-login-workflows-in-expo-go, implement-biometric-login-workflows-in-flutter, implement-biometric-login-workflows-in-react-native, implement-camera-capture-handlers-in-kotlin-android, implement-camera-capture-handlers-in-react-native, implement-keychain-credential-storage-in-expo-go, implement-keychain-credential-storage-in-flutter, implement-push-notifications-hooks-in-expo-go, implement-push-notifications-hooks-in-flutter, implement-push-notifications-hooks-in-kotlin-android, implement-push-notifications-hooks-in-react-native, implement-sqlite-database-local-syncing-in-expo-go, implement-sqlite-database-local-syncing-in-flutter

