# Publish Checklist

Use this checklist before making any repository public.

## Identity and account

- [ ] Git author name does not contain a real name
- [ ] Git author email uses GitHub noreply
- [ ] No public email address is exposed
- [ ] No real face photo is used as avatar
- [ ] No employer, workplace, project, or site name is shown

## Repository content

- [ ] No company name
- [ ] No parent company name
- [ ] No construction site name
- [ ] No location that can identify a real site
- [ ] No real construction site photos
- [ ] No drawings, specifications, estimates, or internal documents
- [ ] No internal emails or client information
- [ ] No real business data

## Files and test data

- [ ] Sample files are dummy data or generated data
- [ ] No real photos are included
- [ ] No EXIF or document metadata exposes personal or work information
- [ ] data/ and output/ are not tracked by Git

## Git history

- [ ] git log --all --format="%ae %an" shows only anonymous author information
- [ ] Commit messages contain no real names, company names, site names, or locations
- [ ] Branch names contain no private information

## README and documentation

- [ ] README describes the project as personal learning or portfolio work
- [ ] README does not imply use of real workplace data
- [ ] README includes a disclaimer if the topic is work-adjacent
- [ ] Usage examples use dummy paths and dummy data

## Final checks

- [ ] python -m pytest passes
- [ ] git status is clean
- [ ] git ls-files does not show private or generated data
- [ ] Repository page looks safe when viewed while logged out
