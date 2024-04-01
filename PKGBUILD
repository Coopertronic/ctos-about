# Maintainer: Matthew Phillip Cooper <coopertronics@gmail.com>

pkgname=about
pkgver=1
pkgrel=1
pkgdesc="This is the about dialog for Coopertronic OS. It givs a breif overview of what Coopertronic OS is all about."
arch=('any')
url="https://coopertronic-ws.ddns.net/ctos-assets/"
license=('custom')
depends=('python' 'pyside6')
source=("$url$pkgname/$pkgname-v$pkgver.zip")
md5sums=('93a95c790a5d784033972daa2e696ca6')

package() {
  ##  Install documentation
  #install -D -m644 $srcdir/README $pkgdir/usr/share/doc/$pkgname/README

  ##  Install licenses
  install -d $pkgdir/usr/share/licenses/$pkgname
  #install -m644 $srcdir/LICENSE $pkgdir/usr/share/licenses/$pkgname/

  ##  Install binaries
  install -d $pkgdir/usr/share/$pkgname
  install -D -m644 $srcdir/scripts/* $pkgdir/usr/share/$pkgname/
  install -D -m755 $srcdir/assets/$pkgname.sh $pkgdir/usr/bin/$pkgname

  ##  Install game icon
  #install -d $pkgdir/usr/share/icons/hicolor/scalable/apps
  #install -D -m644 org.$pkgname.$pkgname.svg $pkgdir/usr/share/icons/hicolor/scalable/apps/org.$pkgname.$pkgname.svg

  ##  Install Application desktop launcher
  install -d $pkgdir/usr/share/applications
  install -D -m644 $srcdir/assets/org.$pkgname.$pkgname.desktop $pkgdir/usr/share/applications/org.$pkgname.$pkgname.desktop
}
